"""
    nllegalcit/parser.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

from lark import Lark

from nllegalcit.citations import Citation, KamerstukCitation
from nllegalcit.visitors import CitationVisitor, CitationVisitorOnlyKamerstukCitations

parser = Lark.open(
    "grammars/citations.lark",
    rel_to=__file__,
    parser="earley"
)


def parse_citations(text: str) -> list[Citation]:
    "Parse any supported citation in a given text"

    parsetree = parser.parse(text)
    v = CitationVisitor()
    v.visit(parsetree)

    return v.citations


def parse_kamerstukcitation(text: str) -> list[KamerstukCitation]:
    "Parse only KamerstukCitations in a given text"

    parsetree = parser.parse(text)
    v = CitationVisitorOnlyKamerstukCitations()
    v.visit(parsetree)

    return v.citations
