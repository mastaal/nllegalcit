"""
    tests/linkextractor/test-oebp23.py

    Test cases for citations to Kamerstukken based on the linkextractor test-oebp23.xslt test
    See:
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/unit/test-oebp23.xslt
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/input/test-oebp23.txt

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit import KamerstukCitation, parse_kamerstukcitation


class Oebp23Test(unittest.TestCase):
    """Test cases for citations to Kamerstukken based on the linkextractor test-oebp23.xslt test"""

    def test_1(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2008-2009, 31 700-VIII, nr. 32, blz. 3"),
            [KamerstukCitation("II", "2008-2009", "31700-VIII", "32", paginaverwijzing="3")]
        )

    def test_2(self):
        self.assertEqual(
            parse_kamerstukcitation("Zie ook kamerstukken II 1999/00, 26 824, nrs. 1–3 pag 4 e v."),
            [KamerstukCitation("II", "1999-2000", "26824", "1-3", paginaverwijzing="4-")]
        )

    def test_3(self):
        self.assertEqual(
            parse_kamerstukcitation("TK 2008-2009, 31473, nummer 25, bladzijde 5 - 6"),
            [KamerstukCitation("II", "2008-2009", "31473", "25", paginaverwijzing="5-6")]
        )

    def test_4(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstuk I 31 145 nummer AA, p. 15"),
            [KamerstukCitation("I", "?", "31145", "AA", paginaverwijzing="15")]
        )

    @unittest.skip("Aanhangsels are not yet supported")
    def test_5(self):
        self.assertEqual(
            parse_kamerstukcitation("Aanhangsel Handelingen TK, 2007/08, nr. 1835, blz 33"),
            []
        )

    @unittest.skip("Handelingen are not yet supported")
    def test_6(self):
        self.assertEqual(
            parse_kamerstukcitation("Handelingen Tweede Kamer 2007-08, nr. 49, p. 3623"),
            []
        )

    def test_7(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 2013-2014, 33037, nr. 80 pagina 123"),
            [KamerstukCitation("II", "2013-2014", "33037", "80", paginaverwijzing="123")]
        )

    def test_8(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2009-2010, 31 930, nr. 68, pag. 4-5"),
            [KamerstukCitation("II", "2009-2010", "31930", "68", paginaverwijzing="4-5")]
        )

    def test_9(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken 11, 1997/1998, 25 672 nr.3 pag.4"),
            [KamerstukCitation("II", "1997-1998", "25672", "3", paginaverwijzing="4")]
        )

    def test_10(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken I 2009-10, 31 560, C, pag. 19"),
            [KamerstukCitation("I", "2009-2010", "31560", "C", paginaverwijzing="19")]
        )

    def test_11(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2008-09, 31 560, nr. 8, pag. 7"),
            [KamerstukCitation("II", "2008-2009", "31560", "8", paginaverwijzing="7")]
        )

    def test_12(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2008-2009, 31 560, nr. 6, p. 17, 19-22"),
            [KamerstukCitation("II", "2008-2009", "31560", "6", paginaverwijzing="17,19-22")]
        )

    def test_13(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken I 2009-2010, 31 560, C, p. 18-19"),
            [KamerstukCitation("I", "2009-2010", "31560", "C", paginaverwijzing="18-19")]
        )

    def test_14(self):
        # No ondernummer given, so not a valid citation
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 2013-2014, 33.950, pag. 2 en 6"),
            []
        )

    def test_15(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, vergaderjaar 2007-2008, 31 386, nr. 3, Memorie van Toelichting, pag. 10"),
            [KamerstukCitation("II", "2007-2008", "31386", "3")]
        )

    @unittest.skip("Handelingen are currently not yet supported")
    def test_16(self):
        self.assertEqual(
            parse_kamerstukcitation("Handelingen II, vergaderjaar 2008-2009, 31 386, nr. 43, pag. 3795"),
            []
        )

    def test_17(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 1989-1990, 21591, nr. 3, pag 69/70"),
            [KamerstukCitation("II", "1989-1990", "21591", "3", paginaverwijzing="69-70")]
        )

    def test_18(self):
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II, 29612, nr. 7, pag 2-3"),
            [KamerstukCitation("II", "?", "29612", "7", paginaverwijzing="2-3")]
        )

    @unittest.skip("Handelingen are currently not yet supported")
    def test_19(self):
        self.assertEqual(
            parse_kamerstukcitation("Handelingen EK 2001-2002, nr. 10, blz. 525"),
            []
        )

    @unittest.skip("Handelingen are currently not yet supported")
    def test_20(self):
        self.assertEqual(
            parse_kamerstukcitation("Handelingen II, 1995-1996, 24 692, nr. 3, p. 14"),
            []
        )

    @unittest.skip("Handelingen are currently not yet supported")
    def test_21(self):
        self.assertEqual(
            parse_kamerstukcitation("Handelingen II, 1996-1997, 24 692, nr. 6, p. 8/9"),
            []
        )

    @unittest.skip("Handelingen are currently not yet supported")
    def test_22(self):
        self.assertEqual(
            parse_kamerstukcitation("Handelingen I, 1996-1997, 24 692, nr. 228b, p. 4"),
            []
        )

    @unittest.skip("Handelingen are currently not yet supported")
    def test_23(self):
        self.assertEqual(
            parse_kamerstukcitation("Handelingen II 2012-2013, nr. 71, item 15, blz 53-69"),
            []
        )
