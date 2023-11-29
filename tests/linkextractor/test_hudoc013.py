"""
    tests/linkextractor/test-hudoc013.py

    Test cases for citations to Kamerstukken based on the linkextractor test-hudoc013.xslt test
    See:
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/unit/test-hudoc013.xslt
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/input/test-hudoc013.txt

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit.citations import EcliCitation
from nllegalcit.parser import parse_citations


class GeneratedTestClass(unittest.TestCase):
    """Test cases for citations to Kamerstukken based on the linkextractor test-hudoc013.xslt test"""

    def test_2(self):
        self.assertEqual(
            parse_citations("Voor Nederlandse uitspraken werkt het: ECLI:NL:HR:2001:AB1838"),
            [EcliCitation("NL", "HR", 2001, "AB1838")]
        )

    def test_3(self):
        self.assertEqual(
            parse_citations("Voor EU-uitspraken werkt het ook: ECLI:EU:C:1997:208"),
            [EcliCitation("EU", "C", 1997, "208")]
        )

    def test_4(self):
        self.assertEqual(
            parse_citations("Maar voor CE-uitspraken (HUDOC) werkt het niet. Bijvoorbeeld: ECLI:CE:ECHR:2007:0515JUD005239199"),
            [EcliCitation("CE", "ECHR", 2007, "0515JUD005239199")]
        )
