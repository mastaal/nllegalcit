#!/usr/bin/env python
"""
    tools/create_initial_test_case_from_pdf_url.py

    Automatically create initial test cases for a pdf given by a URL.

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

import argparse

from nllegalcit.citations import Citation, EcliCitation, KamerstukCitation
from nllegalcit.parser import parse_citations_from_pdf_url

parser = argparse.ArgumentParser(
    prog="create_initial_test_case_from_pdf_url.py",
    description="Automatically create initial test cases for a pdf given by a URL.",
    epilog="Copyright 2023, Martijn Staal, available under the EUPL-1.2 or later."
)

parser.add_argument("url", type=str, nargs="+", help="The URL(s) to create initial test cases for")
parser.add_argument("--startcount", type=int, default=0, help="Optional starting point to count for adding new tests")

args = parser.parse_args()


def create_constructor_for_citation(c: Citation) -> str:
    """Create a string to create an identical object as c"""
    if isinstance(c, EcliCitation):
        return f"EcliCitation(\"{c.country}\", \"{c.court}\", {c.year}, \"{c.casenumber}\")"

    if isinstance(c, KamerstukCitation):
        if c.paginaverwijzing is None and c.rijksdossiernummer is None:
            return f"KamerstukCitation(\"{c.kamer}\", \"{c.vergaderjaar}\", \"{c.dossiernummer}\", \"{c.ondernummer}\")"

        if c.paginaverwijzing is not None and c.rijksdossiernummer is None:
            return f"KamerstukCitation(\"{c.kamer}\", \"{c.vergaderjaar}\", \"{c.dossiernummer}\", \"{c.ondernummer}\", paginaverwijzing=\"{c.paginaverwijzing}\")"

        if c.paginaverwijzing is None and c.rijksdossiernummer is not None:
            return f"KamerstukCitation(\"{c.kamer}\", \"{c.vergaderjaar}\", \"{c.dossiernummer}\", \"{c.ondernummer}\", rijksdossiernummer=\"{c.rijksdossiernummer}\")"

        return f"KamerstukCitation(\"{c.kamer}\", \"{c.vergaderjaar}\", \"{c.dossiernummer}\", \"{c.ondernummer}\", rijksdossiernummer=\"{c.rijksdossiernummer}\", paginaverwijzing=\"{c.paginaverwijzing}\")"


test_count: int = args.startcount

for url in args.url:
    citations = parse_citations_from_pdf_url(url)

    citation_strings = [f"            {create_constructor_for_citation(c)}" for c in citations]

    complete_citation_string = ""
    for cstr in citation_strings:
        complete_citation_string += f"{cstr},\n"

    test_case: str = (f"def test_{test_count}(self):\n"
                      "    self.assertEqual(\n"
                      f"        parse_citations_from_pdf_url(\"{url}\"),\n"
                      "        [\n"
                      f"{complete_citation_string}"
                      "        ]\n"
                      "    )")

    print(test_case)
