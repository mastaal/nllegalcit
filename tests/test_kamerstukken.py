"""
    tests/test_kamerstukken.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long

import unittest

from nllegalcit.kamerstukken import KamerstukCitation, parse_kamerstukcitation


class KamerstukCitationTests(unittest.TestCase):
    """Test cases for the KamerstukCitation parsing"""

    def test_only_citation(self):
        """Test cases with only the clean citation given"""
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2022/23, 36 229, nr. 1"),
            [KamerstukCitation("II", "2022/23", "36229", "1")]
        )
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2020/21, 35 845, nr. 6"),
            [KamerstukCitation("II", "2020/21", "35845", "6")]
        )
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken I 2021/22, 35 925, nr. E"),
            [KamerstukCitation("I", "2021/22", "35925", "E")]
        )
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2020/21, 35 791, nr. 3"),
            [KamerstukCitation("II", "2020/21", "35791", "3")]
        )

    def test_only_citation_with_pagenumber(self):
        """Test cases with only the clean citation given, with page numbers"""
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2005/06, 30 316, nr. 3, p. 7–8"),
            [KamerstukCitation("II", "2005/06", "30316", "3", paginaverwijzing="p. 7–8")]
        )
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2020/21, 35 625, nr. 4, p. 12 en 13"),
            [KamerstukCitation("II", "2020/21", "35625", "4", paginaverwijzing="p. 12 en 13")]
        )
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken II 2005/06, 30 316, nr. 3, p. 5"),
            [KamerstukCitation("II", "2005/06", "30316", "3", paginaverwijzing="p. 5")]
        )

    def test_with_some_other_text(self):
        """KamerstukCitation test cases with some other input in the string"""
        self.assertEqual(
            parse_kamerstukcitation("Zoals te vinden in Kamerstukken II 2005/06, 30 316, nr. 3, p. 5, is algemeen"),
            [KamerstukCitation("II", "2005/06", "30316", "3", paginaverwijzing="p. 5")]
        )
        self.assertEqual(
            parse_kamerstukcitation("  5Kamerstukken II 2005/06, 30 316, nr. 3, p. 5"),
            [KamerstukCitation("II", "2005/06", "30316", "3", paginaverwijzing="p. 5")]
        )
        self.assertEqual(
            parse_kamerstukcitation("   6Meest recente versie opgenomen in Kamerstukken II 2020/21, 35 523, nr. 8"),
            [KamerstukCitation("II", "2020/21", "35523", "8")]
        )
        self.assertEqual(
            parse_kamerstukcitation("                  Uit de nota naar aanleiding van het verslag (Kamerstukken II 2020/21, 35 845, nr. 6"),
            [KamerstukCitation("II", "2020/21", "35845", "6")]
        )
        self.assertEqual(
            parse_kamerstukcitation("                  van nota naar aanleiding van verslag; Kamerstukken II 2020/21, 35 845, nr. 6"),
            [KamerstukCitation("II", "2020/21", "35845", "6")]
        )
        self.assertEqual(
            parse_kamerstukcitation("               1Bijlage bij Kamerstukken II 2021/22, 29 628, nr. 1051"),
            [KamerstukCitation("II", "2021/22", "29628", "1051")]
        )
        self.assertEqual(
            parse_kamerstukcitation("               1Kamerstukken II 2021/2022, 35 925 IV, nr. 26"),
            [KamerstukCitation("II", "2021/2022", "35925IV", "26")]
        )
        self.assertEqual(
            parse_kamerstukcitation("               44Ontwerp-Miljoenennota 2020, Kamerstukken II 2019/20, 35 300, nr. 3"),
            [KamerstukCitation("II", "2019/20", "35300", "3")]
        )
        self.assertEqual(
            parse_kamerstukcitation("                  (Commissie Van Beek). Zie: Kamerstukken II 2013/14, 31 142, nr. 37"),
            [KamerstukCitation("II", "2013/14", "31142", "37")]
        )

    def test_with_other_text_with_special_characters(self):
        """KamerstukCitation test cases with some other input with special chracters in the string"""
        self.assertEqual(
            parse_kamerstukcitation("                  geliberaliseerde huurovereenkomsten» (Kamerstukken II 2019/20, 35 488, nr. 2"),
            [KamerstukCitation("II", "2019/20", "35488", "2")]
        )

    def test_multiple_full_citations_in_text(self):
        """KamerstukCitation test with multiple full citations at once"""
        self.assertEqual(
            parse_kamerstukcitation("               6Kamerstukken II 2005/06, 30 316, nr. 3, p. 5 en vgl. Kamerstukken II, 2005/06, 30 316, nr. 6"),
            [KamerstukCitation("II", "2005/06", "30316", "3", paginaverwijzing="p. 5"), KamerstukCitation("II", "2005/06", "30316", "6")]
        )
        self.assertEqual(
            parse_kamerstukcitation("               4Bijlage bij Kamerstukken II 2013/14, 31 142, nr. 37; bijlage bij Kamerstukken II 2015/16, 31 142, nr. 55 en bijlage bij Kamerstukken II 2018/19, 35 165, nr. 4"),
            [KamerstukCitation("II", "2013/14", "31142", "37"), KamerstukCitation("II", "2015/16", "31142", "55"), KamerstukCitation("II", "2018/19", "35165", "4")]
        )

    @unittest.skip("Multiple shorthand citations are currently not yet supported")
    def test_with_multiple_citations_shorthand(self):
        """Multiple citations in a shorthand notation. Currently not supported."""

        self.assertEqual(
            parse_kamerstukcitation("               1Kamerstukken II 2020/21, 35 625, nr. 4, p. 12 en 13, en nr. 6"),
            [
                KamerstukCitation("II", "2020/21", "35625", "4", paginaverwijzing="p. 12 en 13"),
                KamerstukCitation("II", "2020/21", "35625", "6")
            ]
        )
