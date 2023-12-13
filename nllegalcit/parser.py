"""
    nllegalcit/parser.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

import io
import pathlib
from typing import Any, IO

import requests

from lark import Lark
from pypdf import PdfReader

from .citations import Citation, KamerstukCitation
from .visitors import CitationVisitor, CitationVisitorOnlyKamerstukCitations

parser = Lark.open(
    "grammars/citations.lark",
    rel_to=__file__,
    parser="earley"
)


def parse_citations(text: str) -> list[Citation]:
    """Parse any supported citation in a given text."""

    parsetree = parser.parse(text)
    v = CitationVisitor()
    v.visit(parsetree)

    return v.citations


def parse_citations_from_pdf(pdffile: str | IO[Any] | pathlib.Path) -> list[Citation]:
    """Parse any supported citations in a given PDF file.

    Reading the PDF file is done via pypdf. The pdffile may be any file object or a path
    to the pdf file.
    """

    reader = PdfReader(pdffile)

    pdf_text: str = ""

    for page in reader.pages:
        pdf_text += page.extract_text()

    return parse_citations(pdf_text)


def parse_citations_from_pdf_url(url: str) -> list[Citation]:
    """Parse any supported citations in a PDF which is located at the given URL."""

    pdf_response = requests.get(url)

    return parse_citations_from_pdf(io.BytesIO(pdf_response.content))


def parse_kamerstukcitation(text: str) -> list[KamerstukCitation]:
    """Parse only KamerstukCitations in a given text."""

    parsetree = parser.parse(text)
    v = CitationVisitorOnlyKamerstukCitations()
    v.visit(parsetree)

    return v.citations
