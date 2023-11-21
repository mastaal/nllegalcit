"""
    nllegalcit/kamerstukken.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

from enum import Enum
import logging
import re

from lark import Lark, Visitor, ParseTree

from nllegalcit.errors import CitationParseException

logger = logging.getLogger(__name__)
re_whitespace: re.Pattern = re.compile(r"\s+")

# TODO: Maybe it's more practical to just move the grammars to inline Python strings?
with open("./nllegalcit/grammars/kamerstukken.lark", "rt", encoding="utf-8") as gf:
    kamerstukken_grammar = gf.read()


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

    def __init__(self, kamer: str, vergaderjaar: str, dossiernummer: str, ondernummer: str, paginaverwijzing=None):
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
            return f"{self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer} {self.paginaverwijzing}"

        return f"{self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer}"

    def __eq__(self, other) -> bool:
        try:
            return (self.kamer == other.kamer) and (self.vergaderjaar == other.vergaderjaar) and (self.dossiernummer == other.dossiernummer) and (self.ondernummer == other.ondernummer)
        except AttributeError:
            return False


class CitationVisitor(Visitor):

    def __init__(self):
        super().__init__()

        self.citations: list[KamerstukCitation] = []

    def kamerstuk(self, tree: ParseTree):
        v = KamerstukCitationVisitor()
        v.visit(tree)
        self.citations.append(v.citation)


class KamerstukCitationVisitor(Visitor):
    """Visitor class to create a KamerstukCitation from the Lark parse tree"""

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
    logger.debug(parsetree.children)
    # print(parsetree)
    v = CitationVisitor()
    v.visit(parsetree)

    return v.citations
