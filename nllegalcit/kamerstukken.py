"""
    nllegalcit/kamerstukken.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

import re

from enum import Enum
from importlib.resources import files

from lark import Lark, Visitor, ParseTree

from nllegalcit.errors import CitationParseException

re_whitespace: re.Pattern = re.compile(r"\s+")

kamerstukken_grammar = files("nllegalcit.grammars").joinpath("kamerstukken.lark").read_text()


class KamerstukCitation:
    """Structured representation of a citation of a kamerstuk"""

    class Kamer(Enum):
        TK = "II"
        EK = "I"
        VV = "VV"

    kamer: Kamer
    vergaderjaar: str
    dossiernummer: str
    ondernummer: str
    paginaverwijzing: str

    def __init__(
            self,
            kamer: str,
            vergaderjaar: str,
            dossiernummer: str,
            ondernummer: str,
            paginaverwijzing=None):
        self.kamer = kamer
        self.vergaderjaar = vergaderjaar
        self.dossiernummer = dossiernummer
        self.ondernummer = ondernummer
        self.paginaverwijzing = paginaverwijzing

    def __str__(self) -> str:
        if self.paginaverwijzing is not None:
            return f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer} {self.paginaverwijzing}"

        return f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer}"

    def __repr__(self) -> str:
        if self.paginaverwijzing is not None:
            return f"Kamerstukken {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer} {self.paginaverwijzing}"

        return f"Kamerstukken {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer}"

    def __eq__(self, other) -> bool:
        try:
            return (self.kamer == other.kamer) and (self.vergaderjaar == other.vergaderjaar) and (self.dossiernummer == other.dossiernummer) and (self.ondernummer == other.ondernummer)
        except AttributeError:
            return False


class CitationVisitor(Visitor):
    """Generic visitor to create Citation objects for a ParseTree"""

    def __init__(self):
        super().__init__()

        self.citations: list[KamerstukCitation] = []

    def kamerstuk(self, tree: ParseTree):
        """Create a KamerstukCitation from a kamerstuk ParseTree rule"""
        v = KamerstukCitationVisitor()
        v.visit(tree)
        self.citations.append(v.citation)


class KamerstukCitationVisitor(Visitor):
    """Visitor class to create a KamerstukCitation from the Lark parse tree"""

    # pylint: disable=missing-function-docstring

    def __init__(self):
        super().__init__()

        self.citation = KamerstukCitation("?", "?", "?", "?")

    def kamer(self, tree: ParseTree):
        if tree.children[0].type == "TK":
            self.citation.kamer = "II"
        elif tree.children[0].type == "EK":
            self.citation.kamer = "I"
        elif tree.children[0].type == "VV":
            self.citation.kamer = "VV"
        else:
            raise CitationParseException("Invalid Kamer in KamerstukCitation")

    def dossiernummer(self, tree: ParseTree):
        self.citation.dossiernummer = re_whitespace.sub("", tree.children[0])

    def vergaderjaar(self, tree: ParseTree):
        self.citation.vergaderjaar = ''.join(tree.children)

    def ondernummer(self, tree: ParseTree):
        self.citation.ondernummer = tree.children[0]

    def paginaverwijzing(self, tree: ParseTree):
        self.citation.paginaverwijzing = ''.join(tree.children)


parser = Lark(
    grammar=kamerstukken_grammar,
    parser="earley"
)


def parse_kamerstukcitation(raw_citation: str) -> list[KamerstukCitation]:
    "Parse a raw kamerstuk citation"

    parsetree = parser.parse(raw_citation)
    v = CitationVisitor()
    v.visit(parsetree)

    return v.citations
