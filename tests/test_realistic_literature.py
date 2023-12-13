"""
    tests/test_realistic_literature.py

    Test cases for all citations based on actual legal articles.

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit import KamerstukCitation, EcliCitation, parse_citations_from_pdf_url


class RealisticLiteratureTests(unittest.TestCase):
    """Test cases for all citations based on actual legal articles."""

    def test_aak_167_strafprocesrecht(self):
        self.assertEqual(
            parse_citations_from_pdf_url("https://scholarlypublications.universiteitleiden.nl/access/item%3A3621460/view"),
            [
                EcliCitation("NL", "HR", 2013, "963"),
                KamerstukCitation("II", "2020-2021", "35871", "3", paginaverwijzing="2-4"),
                KamerstukCitation("I", "2022-2023", "35871", "D"),
                KamerstukCitation("II", "2022-2023", "36327", "2"),
                EcliCitation("NL", "PHR", 2023, "477"),
                EcliCitation("NL", "PHR", 2023, "477"),
                EcliCitation("NL", "HR", 2010, "BL5629")
            ]
        )

    def test_0(self):
        # See https://hdl.handle.net/1887/3564721
        self.assertEqual(
            parse_citations_from_pdf_url("https://scholarlypublications.universiteitleiden.nl/access/item%3A3564722/view"),
            [
                KamerstukCitation("II", "2022-2023", "36222", "3", paginaverwijzing="114-118"),
                KamerstukCitation("II", "2022-2023", "36222", "5"),
                KamerstukCitation("II", "2021-2022", "35991", "3", paginaverwijzing="3"),
                KamerstukCitation("II", "2021-2022", "35991", "6", paginaverwijzing="5"),
                KamerstukCitation("II", "2021-2022", "31015", "263", paginaverwijzing="2"),
                KamerstukCitation("II", "2021-2022", "31015", "263", paginaverwijzing="4"),
                KamerstukCitation("II", "2021-2022", "31015", "263", paginaverwijzing="3"),
                KamerstukCitation("II", "2022-2023", "28638", "213"),
                KamerstukCitation("II", "2022-2023", "36222", "5"),
                KamerstukCitation("II", "2022-2023", "36222", "6")  # On p. 7, note 10, there is a reference with a combined dossiernummer: "Kamerstukken II 2022/23, 36222 en 31015, nr. 6"
            ]
        )

    def test_1(self):
        # See https://hdl.handle.net/1887/3563008
        # Note that there are some mistakes in some citations, e.g. "HR 23 maart 2012, ECLI:NL:HR:2012, BV0614, NJ 2012/421 (ING Bank/Manning q.q.)"
        # TODO: Double check if these are indeed all citations in this publication
        self.assertEqual(
            parse_citations_from_pdf_url("https://scholarlypublications.universiteitleiden.nl/access/item%3A3563009/view"),
            [
                EcliCitation("NL", "HR", 1975, "AB4313"),
                EcliCitation("NL", "HR", 1987, "AC0457"),
                EcliCitation("NL", "HR", 1987, "AC0457"),
                EcliCitation("NL", "HR", 1989, "AD0705"),
                EcliCitation("NL", "HR", 1989, "AD0705"),
                EcliCitation("NL", "HR", 1990, "AD1065"),
                EcliCitation("NL", "HR", 1992, "ZC0615"),
                EcliCitation("NL", "HR", 1995, "ZC1641"),
                EcliCitation("NL", "HR", 1995, "ZC1641"),
                EcliCitation("NL", "HR", 2004, "AO7575"),
                EcliCitation("NL", "HR", 2004, "AO7575"),
                EcliCitation("NL", "HR", 2004, "AR1943"),
                EcliCitation("NL", "HR", 2004, "AR3137"),
                EcliCitation("NL", "HR", 2005, "AS2688"),
                EcliCitation("NL", "HR", 2006, "AV0653"),
                EcliCitation("NL", "HR", 2006, "AV0653"),
                EcliCitation("NL", "HR", 2006, "AV0653"),
                EcliCitation("NL", "HR", 2012, "BU6552"),
                EcliCitation("NL", "HR", 2013, "BZ5663"),
                EcliCitation("NL", "HR", 2013, "BZ5663"),
                EcliCitation("NL", "HR", 2013, "BZ5663"),
                EcliCitation("NL", "HR", 2014, "319"),
                EcliCitation("NL", "HR", 2015, "3023"),
                EcliCitation("NL", "HR", 2015, "3094"),
                EcliCitation("NL", "HR", 2015, "689"),
                EcliCitation("NL", "HR", 2015, "689"),
                EcliCitation("NL", "HR", 2018, "2189"),
                EcliCitation("NL", "HR", 2018, "2189"),
                EcliCitation("NL", "HR", 2022, "80"),
                EcliCitation("NL", "HR", 2022, "80"),
                KamerstukCitation("II", "2018-2019", "35225", "3", paginaverwijzing="47"),
            ]
        )
