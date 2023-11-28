"""
    nllegalcit/visitors.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

import re
from typing import Optional

from lark import Visitor, ParseTree, Token

from nllegalcit.citations import Citation, KamerstukCitation, CaseLawCitation, EcliCitation
from nllegalcit.errors import CitationParseException

re_dossiernummer_separator: re.Pattern = re.compile(r"[-.\s]+")
re_replacement_toevoeging_separator: re.Pattern = re.compile(r"[.\s-]+")


class CitationVisitor(Visitor):
    """Generic visitor to create Citation objects for a ParseTree"""

    def __init__(self):
        super().__init__()

        self.citations: list[Citation] = []

    def kamerstuk(self, tree: ParseTree):
        """Create a KamerstukCitation from a kamerstuk ParseTree rule"""
        v = KamerstukCitationVisitor()
        v.visit(tree)
        self.citations.append(v.citation)

    def case_law(self, tree: ParseTree):
        """Create a CaseLawCitation from a case_law parse rule"""
        v = CaseLawCitationVisitor()
        v.visit(tree)
        if v.citation is not None:
            self.citations.append(v.citation)


class CaseLawCitationVisitor(Visitor):
    """Visitor class to create a CaseLawCitation from the parse tree"""

    # pylint: disable=missing-function-docstring

    citation: Optional[CaseLawCitation]

    def __init__(self):
        super().__init__()

        self.citation = None

    def caselaw__nl_ecli(self, tree: ParseTree):
        print(tree.children)

        cit = EcliCitation("NL", "?", -1, "?")

        for child in tree.children:
            if isinstance(child, Token):
                if child.type == "caselaw__ECLI_YEAR":
                    cit.year = int(child)
                elif child.type == "caselaw__NL_ECLI_COURT":
                    # TODO: Implement court name normalization
                    cit.court = str(child)
                elif child.type == "caselaw__NL_ECLI_CASENUMBER":
                    cit.casenumber = str(child)

        self.citation = cit


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
            self.citation.dossiernummer = str(dossiernummer)
        else:
            self.citation.dossiernummer = f"{dossiernummer}-{dossiernummer_toevoeging}"

    def kamerstukken__vergaderjaar(self, tree: ParseTree):
        first_year = None
        second_year = None

        for c in tree.children:
            if first_year is None and c.type == "kamerstukken__JAAR4":
                first_year = str(c)
            elif c.type == "kamerstukken__JAAR4":
                second_year = str(c)
            elif c.type == "kamerstukken__JAAR2":
                if first_year == "1999":
                    second_year = "2000"
                elif first_year == "1899":
                    second_year = "1900"
                else:
                    second_year = f"{first_year[0:2]}{str(c)}"

        self.citation.vergaderjaar = f"{first_year}-{second_year}"

    def kamerstukken__ondernummer(self, tree: ParseTree):
        self.citation.ondernummer = tree.children[0]

    def kamerstukken__paginaverwijzing(self, tree: ParseTree):
        paginas_los: list[str] = []
        for c in tree.children:
            try:
                if c.type == "kamerstukken__PAGINA_LOS":
                    paginas_los.append(str(c))
            except AttributeError:
                pass
        pagina_ranges: list[str] = []
        for c in tree.children:
            try:
                if c.data == "kamerstukken__pagina_range":
                    start = None
                    end = None
                    for d in c.children:
                        if d.type == "kamerstukken__PAGINA_START":
                            start = str(d)
                        elif d.type == "kamerstukken__PAGINA_EIND":
                            end = str(d)
                    if end is None:
                        pagina_ranges.append(f"{start}-")
                    else:
                        pagina_ranges.append(f"{start}-{end}")
            except AttributeError:
                pass
        paginas = paginas_los + pagina_ranges
        if len(paginas) == 1:
            self.citation.paginaverwijzing = paginas[0]
        else:
            self.citation.paginaverwijzing = ','.join(paginas)


class CitationVisitorOnlyKamerstukCitations(Visitor):
    """Generic visitor to create Citation objects for a ParseTree"""

    def __init__(self):
        super().__init__()

        self.citations: list[KamerstukCitation] = []

    def kamerstuk(self, tree: ParseTree):
        """Create a KamerstukCitation from a kamerstuk ParseTree rule"""
        v = KamerstukCitationVisitor()
        v.visit(tree)
        self.citations.append(v.citation)
