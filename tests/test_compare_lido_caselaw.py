"""
    tests/test_compare_lido_caselaw.py

    Test cases to compare the performance of nllegalcit with LiDO with regards to
    finding citations to other case law.

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import json
import unittest
import xml.etree.ElementTree as ET

import requests

from bs4 import BeautifulSoup

from nllegalcit import Citation, KamerstukCitation, EcliCitation, parse_citations, ecli_citation_from_correct_string

XML_NAMESPACES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dct": "http://purl.org/dc/terms/",
    "overheidrl": "http://linkeddata.overheid.nl/terms/",
    "lx": "http://linkeddata.overheid.nl/lx/"
}


def caselaw_get_lido_citations(id: str) -> list[EcliCitation]:
    """Request the outgoing Ecli citations that LiDO found for a court decision"""

    url = f"https://linkeddata.overheid.nl/terms/jurisprudentie/id/{id}"
    resp = requests.get(url, timeout=30)
    root = ET.fromstring(resp.text)

    overheidrl_linkt_elems = root.findall("rdf:Description/overheidrl:linkt", XML_NAMESPACES)

    ecli_citations: list[EcliCitation] = []
    for elem in overheidrl_linkt_elems:
        resource = elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource", "No resource found")

        if resource.startswith("http://linkeddata.overheid.nl/terms/jurisprudentie/id/ECLI"):
            # We assume that this is a correctly formatted ECLI
            ecli_citations.append(ecli_citation_from_correct_string(resource[55:]))

    return ecli_citations


def uitspraken_get_ecli_citations(ecli: str) -> list[EcliCitation]:
    """Find all EcliCitations for a Dutch court decision using nllegalcit"""

    url = f"https://uitspraken.rechtspraak.nl/api/document/?id={ecli}"
    resp = requests.get(url, timeout=30)
    info = json.loads(resp.text)

    plaintext = BeautifulSoup(info["UitspraakTekst"], "html.parser").get_text()

    citations = parse_citations(plaintext)

    ecli_citations: list[EcliCitation] = []
    for cit in citations:
        if isinstance(cit, EcliCitation):
            ecli_citations.append(cit)

    return ecli_citations


class LidoComparisonCaseLawTests(unittest.TestCase):
    """Test cases to compare the performance of nllegalcit with LiDO with regards to
    finding citations to other case law.
    """

    def test_nl_hr_2021_656(self):
        self.assertEqual(
            caselaw_get_lido_citations("ECLI:NL:HR:2021:656"),
            uitspraken_get_ecli_citations("ECLI:NL:HR:2021:656")
        )

    def test_nl_hr_2015_3019(self):
        self.assertEqual(
            caselaw_get_lido_citations("ECLI:NL:HR:2015:3019"),
            uitspraken_get_ecli_citations("ECLI:NL:HR:2015:3019")
        )

    def test_nl_rbdha_2022_4119(self):
        ecli = "ECLI:NL:RBDHA:2022:4119"
        self.assertEqual(
            caselaw_get_lido_citations(ecli),
            uitspraken_get_ecli_citations(ecli)
        )
