"""
    tests/linkextractor/test_oebp12.py

    Test cases for citations to Kamerstukken based on the linkextractor test-oebp11.xslt test
    See:
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/unit/test-oebp12.xslt
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/input/test-oebp12.txt

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit.citations import KamerstukCitation
from nllegalcit.parser import parse_kamerstukcitation


class Oebp11Test(unittest.TestCase):
    """Test cases for citations to Kamerstukken based on the linkextractor test-oebp11.xslt test"""

    def test_1(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken I, 2008-2009, 31145, nr. C"),
            [KamerstukCitation("I", "2008-2009", "31145", "C")]
        )

    def test_2(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken EK, 2014-2015, 31 145, AA"),
            [KamerstukCitation("I", "2014-2015", "31145", "AA")]
        )

    def test_3(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken Eerste Kamer 2014-15, 31 145, AA"),
            [KamerstukCitation("I", "2014-2015", "31145", "AA")]
        )

    def test_4(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken Eerste Kamer 31145 nr AA"),
            [KamerstukCitation("I", "?", "31145", "AA")]
        )

    def test_4a(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken Eerste Kamer 31145 nr. AA"),
            [KamerstukCitation("I", "?", "31145", "AA")]
        )

    def test_5(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstuk I 31145 AA"),
            [KamerstukCitation("I", "?", "31145", "AA")]
        )

    def test_6(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstuk I 31145, AA"),
            [KamerstukCitation("I", "?", "31145", "AA")]
        )

    def test_7(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstuk I 31 145 nummer AA, p. 15"),
            [KamerstukCitation("I", "?", "31145", "AA", paginaverwijzing="15")]
        )

    def test_8(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 31 700-IIB, nr 2"),
            [KamerstukCitation("II", "?", "31700-IIB", "2")]
        )

    def test_9(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 21501-20, nr. 917"),
            [KamerstukCitation("II", "?", "21501-20", "917")]
        )
