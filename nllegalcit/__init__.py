"""
    nllegalcit/__init__.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# mypy: disable-error-code="name-defined"

from .citations import Citation, CaseLawCitation, EcliCitation, KamerstukCitation
from .parser import parse_citations, parse_citations_from_pdf, parse_citations_from_pdf_url, parse_kamerstukcitation
from .errors import CitationParseException

del visitors  # pylint: disable=undefined-variable
del errors  # pylint: disable=undefined-variable
del citations  # pylint: disable=undefined-variable
del parser  # pylint: disable=undefined-variable
del utils  # pylint: disable=undefined-variable

__all__ = ["Citation", "CaseLawCitation", "EcliCitation", "KamerstukCitation",
           "parse_citations", "parse_citations_from_pdf", "parse_citations_from_pdf_url", "parse_kamerstukcitation",
           "CitationParseException"]
