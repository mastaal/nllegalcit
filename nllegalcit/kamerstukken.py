"""
    nllegalcit/kamerstukken.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

import re

from enum import Enum
from importlib.resources import files
from typing import Optional

from lark import Lark, Visitor, ParseTree

from nllegalcit.errors import CitationParseException

re_dossiernummer_separator: re.Pattern = re.compile(r"[-.\s]+")
re_replacement_toevoeging_separator: re.Pattern = re.compile(r"[.\s-]+")

kamerstukken_grammar = files("nllegalcit.grammars").joinpath("citations.lark").read_text()


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
    paginaverwijzing: Optional[str]
    rijksdossiernummer: Optional[str]

    def __init__(
            self,
            kamer: str,
            vergaderjaar: str,
            dossiernummer: str,
            ondernummer: str,
            paginaverwijzing=None,
            rijksdossiernummer=None):
        self.kamer = kamer
        self.vergaderjaar = vergaderjaar
        self.dossiernummer = dossiernummer
        self.ondernummer = ondernummer
        self.paginaverwijzing = paginaverwijzing
        self.rijksdossiernummer = rijksdossiernummer

    def __str__(self) -> str:
        # There surely must be a better way to do this
        if self.rijksdossiernummer is not None and self.paginaverwijzing is not None:
            return (f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer}"
                    f" ({self.rijksdossiernummer}) {self.ondernummer} {self.paginaverwijzing}")
        if self.paginaverwijzing is not None:
            return (f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer}"
                    f"{self.ondernummer} {self.paginaverwijzing}")
        if self.rijksdossiernummer is not None:
            return (f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer}"
                    f" ({self.rijksdossiernummer}) {self.ondernummer}")

        return f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer}"

    def __repr__(self) -> str:
        if self.paginaverwijzing is not None:
            return f"Kamerstukken {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer} {self.paginaverwijzing}"

        return f"Kamerstukken {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer}"

    def __eq__(self, other) -> bool:
        try:
            return ((self.kamer == other.kamer) and
                    (self.vergaderjaar == other.vergaderjaar) and
                    (self.dossiernummer == other.dossiernummer) and
                    (self.ondernummer == other.ondernummer) and
                    (self.paginaverwijzing == other.paginaverwijzing) and
                    (self.rijksdossiernummer == other.rijksdossiernummer))
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

    def kamerstukken__kamer(self, tree: ParseTree):
        if tree.children[0].type == "kamerstukken__TK":
            self.citation.kamer = "II"
        elif tree.children[0].type == "kamerstukken__EK":
            self.citation.kamer = "I"
        elif tree.children[0].type == "kamerstukken__VV":
            self.citation.kamer = "VV"
        else:
            raise CitationParseException("Invalid Kamer in KamerstukCitation")

    def kamerstukken__dossiernummer(self, tree: ParseTree):
        dossiernummer = "?"
        dossiernummer_toevoeging: Optional[str] = None
        for c in tree.children:
            if c.type == "kamerstukken__DOSSIERNUMMER":
                dossiernummer = re_dossiernummer_separator.sub("", c)
            elif c.type == "kamerstukken__DOSSIERNUMMER_TOEVOEGING":
                dossiernummer_toevoeging = re_replacement_toevoeging_separator.sub("", c).replace("hoofdstuk", "")

        if dossiernummer_toevoeging is None:
            self.citation.dossiernummer = dossiernummer
        else:
            self.citation.dossiernummer = f"{dossiernummer}-{dossiernummer_toevoeging}"

    def kamerstukken__vergaderjaar(self, tree: ParseTree):
        first_year = None
        second_year = None

        for c in tree.children:
            if first_year is None and c.type == "kamerstukken__JAAR4":
                first_year = c
            elif c.type == "kamerstukken__JAAR4":
                second_year = c
            elif c.type == "kamerstukken__JAAR2":
                if first_year == "1999":
                    second_year = "2000"
                elif first_year == "1899":
                    second_year = "1900"
                else:
                    second_year = f"{first_year[0:2]}{c}"

        self.citation.vergaderjaar = f"{first_year}-{second_year}"

    def kamerstukken__ondernummer(self, tree: ParseTree):
        self.citation.ondernummer = tree.children[0]

    def kamerstukken__paginaverwijzing(self, tree: ParseTree):
        self.citation.paginaverwijzing = ''.join(tree.children)


parser = Lark.open(
    "grammars/citations.lark",
    rel_to=__file__,
    parser="earley"
)


def parse_kamerstukcitation(raw_citation: str) -> list[KamerstukCitation]:
    "Parse a raw kamerstuk citation"

    parsetree = parser.parse(raw_citation)
    v = CitationVisitor()
    v.visit(parsetree)

    return v.citations
