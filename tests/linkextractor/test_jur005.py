"""
    tests/linkextractor/test-jur005.py

    Test cases for citations to case law using ECLI's based on the linkextractor test-jur005.xslt test
    See:
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/unit/test-jur005.xslt
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/input/test-jur005.txt

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit.citations import EcliCitation
from nllegalcit.parser import parse_citations


class GeneratedTestClass(unittest.TestCase):
    """Test cases for citations to Kamerstukken based on the linkextractor test-jur005.xslt test"""

    def test_2(self):
        self.assertEqual(
            parse_citations("ECLI:NL:HR:2010:392"),
            [EcliCitation("NL", "HR", 2010, "392")]
        )

    def test_3(self):
        self.assertEqual(
            parse_citations("ECLI:Nl:Hr:2010:28"),
            [EcliCitation("NL", "HR", 2010, "28")]
        )

    def test_4(self):
        self.assertEqual(
            parse_citations("ECLI:NL:RBROT:2010:AB3492"),
            [EcliCitation("NL", "RBROT", 2010, "AB3492")]
        )

    def test_5(self):
        self.assertEqual(
            parse_citations("ECLI: NL:HR:2010:392"),
            [EcliCitation("NL", "HR", 2010, "392")]
        )

    def test_6(self):
        self.assertEqual(
            parse_citations("ECLI:NL:HR:2010: 392"),
            [EcliCitation("NL", "HR", 2010, "392")]
        )

    def test_7(self):
        self.assertEqual(
            parse_citations("ECLI : NL:HR:2010:392"),
            [EcliCitation("NL", "HR", 2010, "392")]
        )

    def test_8(self):
        self.assertEqual(
            parse_citations("ECLI:NL:HR:1973:ZF3911"),
            [EcliCitation("NL", "HR", 1973, "ZF3911")]
        )

    def test_9(self):
        self.assertEqual(
            parse_citations("ECLI:NL:RvS:1984:AH0317"),
            [EcliCitation("NL", "RvS", 1984, "AH0317")]
        )

    def test_10(self):
        self.assertEqual(
            parse_citations("NL:RvS:1984:AH0317"),
            [EcliCitation("NL", "RvS", 1984, "AH0317")]
        )

    def test_11(self):
        self.assertEqual(
            parse_citations("RVS:1984:AH0317"),
            [EcliCitation("NL", "RvS", 1984, "AH0317")]
        )
