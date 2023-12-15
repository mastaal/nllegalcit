"""
    tests/linkextractor/test-jur004.py

    Test cases for citations to Kamerstukken based on the linkextractor test-jur004.xslt test
    See:
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/unit/test-jur004.xslt
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/input/test-jur004.txt

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit import LjnCitation, parse_citations


class Jur004TestCases(unittest.TestCase):
    """Test cases for citations to Kamerstukken based on the linkextractor test-jur004.xslt test"""

    def test_2(self):
        self.assertEqual(
            parse_citations("LJN AB1234"),
            [LjnCitation("AB1234")]
        )

    def test_3(self):
        self.assertEqual(
            parse_citations("LJN: AB4535"),
            [LjnCitation("AB4535")]
        )

    def test_4(self):
        self.assertEqual(
            parse_citations("LJN RB4930"),
            [LjnCitation("RB4930")]
        )

    def test_5(self):
        self.assertEqual(
            parse_citations("ljn AB2345"),
            [LjnCitation("AB2345")]
        )

    def test_6(self):
        self.assertEqual(
            parse_citations("LJN-nummer AB2134"),
            [LjnCitation("AB2134")]
        )

    def test_7(self):
        self.assertEqual(
            parse_citations("LJ-nummer AF3483"),
            [LjnCitation("AF3483")]
        )

    def test_8(self):
        self.assertEqual(
            parse_citations("LJN-nr AJ9403"),
            [LjnCitation("AJ9403")]
        )

    def test_9(self):
        self.assertEqual(
            parse_citations("LJN-nr. AJ4938"),
            [LjnCitation("AJ4938")]
        )

    def test_10(self):
        self.assertEqual(
            parse_citations("LJ-nr AB3493"),
            [LjnCitation("AB3493")]
        )

    def test_11(self):
        self.assertEqual(
            parse_citations("LJN ej3832"),
            [LjnCitation("EJ3832")]
        )

    def test_12(self):
        self.assertEqual(
            parse_citations("lj nr. AF3232"),
            [LjnCitation("AF3232")]
        )

    def test_13(self):
        self.assertEqual(
            parse_citations("LJN nummer AB3929"),
            [LjnCitation("AB3929")]
        )

    def test_14(self):
        self.assertEqual(
            parse_citations("ljn: Ab 3948"),
            [LjnCitation("AB3948")]
        )

    def test_15(self):
        self.assertEqual(
            parse_citations("ELRO AA5776"),
            [LjnCitation("AA5776")]
        )

    def test_16(self):
        self.assertEqual(
            parse_citations("ELRO nummer AA9162"),
            [LjnCitation("AA9162")]
        )

    def test_17(self):
        self.assertEqual(
            parse_citations("ELRO-nummer AA9162"),
            [LjnCitation("AA9162")]
        )

    def test_18(self):
        self.assertEqual(
            parse_citations("ELRO-nummer AA 9162"),
            [LjnCitation("AA9162")]
        )

    def test_19(self):
        self.assertEqual(
            parse_citations("ELRO-nr AA 9162"),
            [LjnCitation("AA9162")]
        )

    def test_20(self):
        self.assertEqual(
            parse_citations("ELRO ZD 1846"),
            [LjnCitation("ZD1846")]
        )

    def test_21(self):
        self.assertEqual(
            parse_citations("ELRO nr. AA 8200"),
            [LjnCitation("AA8200")]
        )
