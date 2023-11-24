"""
    tests/linkextractor/test_oebp11.py

    Test cases for citations to Kamerstukken based on the linkextractor test-oebp11.xslt test
    See:
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/unit/test-oebp11.xslt
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/input/test-oebp11.txt

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit.kamerstukken import KamerstukCitation, parse_kamerstukcitation


class Oebp11Test(unittest.TestCase):
    """Test cases for citations to Kamerstukken based on the linkextractor test-oebp11.xslt test"""

    def test_1(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2008-2009, 31 700-VIII, nr. 32, blz. 3"),
            [KamerstukCitation("II", "2008-2009", "31700-VIII", "32", paginaverwijzing="3")]
        )

    # Note that the linkextractor apparantly normalizes the year notation
    def test_2(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 2008/09, 31700.VIII, 32"),
            [KamerstukCitation("II", "2008-2009", "31700-VIII", "32")]
        )

    def test_3(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken Tweede Kamer 31-700 XII nr 6"),
            [KamerstukCitation("II", "?", "31700-XII", "6")]
        )

    def test_4(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstuk TK 31.700XII, 6"),
            [KamerstukCitation("II", "?", "31700-XII", "6")]
        )

    def test_5(self):
        self.assertEqual(
            parse_kamerstukcitation("TK 2008-2009, 31473, nummer 25"),
            [KamerstukCitation("II", "2008-2009", "31473", "25")]
        )

    def test_6(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 2008/09 34 473 nr. 251"),
            [KamerstukCitation("II", "2008-2009", "34473", "251")]
        )

    def test_7(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken 2, 2008-2009, 31459, 22"),
            [KamerstukCitation("II", "2008-2009", "31459", "22")]
        )

    def test_8(self):
        self.assertEqual(
            parse_kamerstukcitation("Tweede Kamer 2008-2009, 31459, 22"),
            [KamerstukCitation("II", "2008-2009", "31459", "22")]
        )

    def test_9(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 31 459 22"),
            [KamerstukCitation("II", "?", "31459", "22")]
        )
