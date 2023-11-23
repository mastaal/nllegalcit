"""
    tests/test_kamerstukken.py

    Test cases for citations to Kamerstukken.

    Nearly all of these citations are actual citations found in the Kamerstukken.

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
        self.assertEqual(
            parse_kamerstukcitation("Kamerstukken I 1979/80, 15 516, nr. 42e, blz. 7"),
            [KamerstukCitation("I", "1979/80", "15516", "42e", paginaverwijzing="blz. 7")]
        )

    def test_in_context_recent(self):
        """KamerstukCitation test cases within a textual context from recent sources"""

        self.assertEqual(
            parse_kamerstukcitation("               1Kamerstukken II 2001/02, 28 295, nr. 1"),
            [KamerstukCitation("II", "2001/02", "28295", "1")]
        )

        self.assertEqual(
            parse_kamerstukcitation("               32Advies van de Afdeling advisering van 9 december 2016, Kamerstukken II 2016/17, 34 673, nr. 4"),
            [KamerstukCitation("II", "2016/17", "34673", "4")]
        )

        self.assertEqual(
            parse_kamerstukcitation("               10Zie voor meer toelichting over deze instrumenten Kamerstukken II 2014/15, 34 208, nr. 3"),
            [KamerstukCitation("II", "2014/15", "34208", "3")]
        )

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
            [KamerstukCitation("II", "2021/2022", "35925-IV", "26")]
        )
        self.assertEqual(
            parse_kamerstukcitation("               44Ontwerp-Miljoenennota 2020, Kamerstukken II 2019/20, 35 300, nr. 3"),
            [KamerstukCitation("II", "2019/20", "35300", "3")]
        )
        self.assertEqual(
            parse_kamerstukcitation("                  (Commissie Van Beek). Zie: Kamerstukken II 2013/14, 31 142, nr. 37"),
            [KamerstukCitation("II", "2013/14", "31142", "37")]
        )

    def test_in_context_older(self):
        """KamerstukCitation test cases within a textual context from older sources"""
        self.assertEqual(
            parse_kamerstukcitation("5.3.2. Voorts houdt de Memorie van Antwoord (Kamerstukken II, 1987/1988, 20 074, nr. 6, blz. 19–20) onder meer in: "),
            [KamerstukCitation("II", "1987/1988", "20074", "6", paginaverwijzing="blz. 19–20")]
        )
        self.assertEqual(
            parse_kamerstukcitation(""" gegeven toelichting ertoe strekte het begrip aftrekbare kosten aan te scherpen
                                    (Kamerstukken II, 1988/89, 20 873, nr. 39). 3.5. In het verdere verloop van de parlementaire
                                    behandeling zijn met betrekking tot dit amendement in het bijzonder de arresten van de Hoge
                                    Raad van 30 november 1977, nr. 18 586, BNB 1978/7, en van 7 mei 1980, nr. 19 874, BNB 1980/186,
                                    ter sprake gebracht (Handelingen II, 1988/89, blz. 39-2410 en 2435 en
                                    Handelingen UCV, 1988/89, nr. 26, blz. 50 en 53)."""),
            [KamerstukCitation("II", "1988/89", "20873", "39")]
        )
        self.assertEqual(
            parse_kamerstukcitation("6.2. Ter toelichting werd opgemerkt (Kamerstukken II, Zitting 1958-1959-5380, Nr. 3, blz. 41, slot lk.):"),
            [KamerstukCitation("II", "1958-1959", "5380", "3", paginaverwijzing="blz. 41")]
        )
        self.assertEqual(
            parse_kamerstukcitation(""" Door de Regering is hierop in de Tweede Kamer als volgt gereageerd (Memorie van Antwoord,
                                    Kamerstukken II, 1985/- 86, 19 559, nr. 6, blz. 7): "De door ons in artikel III voorgestelde
                                    regeling is, zoals"""),
            [KamerstukCitation("II", "1985/- 86", "19559", "6", paginaverwijzing="blz. 7")]
        )
        self.assertEqual(
            parse_kamerstukcitation(""" Hetgeen in punt 4.6 van de Conclusie van de Advocaat- Generaal omtrent de wetsgeschiedenis
                                    is vermeld is hiermede in overeenstemming, al noopt hetgeen aldaar is vermeld uit de Nadere
                                    Memorie van Antwoord aan de Eerste Kamer (Kamerstukken I 1979/80, 15 516, nr. 42e, blz. 7) wel
                                    ertoe in gevallen waarin een vennootschap werkzaamheden van uiteenlopende aard verricht"""),
            [KamerstukCitation("I", "1979/80", "15516", "42e", paginaverwijzing="blz. 7")]
        )
        # Not sure yet what this should be
        # self.assertEqual(
        #     parse_kamerstukcitation("""9 Zie Minister Polak in de Eerste Kamer
        #                             (Kamerstukken I, 1969-1970, 9595,9596, blz 1092): De mogelijkheid
        #                             van het aanvragen van een enquête zal naar ik hoop en verwacht vooral
        #                             preventief werken en misstanden voorkomen, misstanden, die gelukkig in het
        #                             Nederlandse bedrijfsleven slechts sporadisch voorkomen."""),
        #     [KamerstukCitation("I", "1969-1970", "9595,9596")]
        # )

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

    def test_citation_to_eu_council_dossier(self):
        """KamerstukCitation test for EU Council dossiers, which have a particular dossiernumber of the form 21 501-07"""
        # Note that the first citation does not provide a document number, and is thus ignored.
        self.assertEqual(
            parse_kamerstukcitation("               1Kamerstukken II 2020/21, 35570 en Kamerstukken II 2020/21, 21 501-07, nr. 1750"),
            [KamerstukCitation("II", "2020/21", "21501-07", "1750")]
        )

        self.assertEqual(
            parse_kamerstukcitation("               38Voorjaarsrapportage 2021, Kamerstukken II 2020/21, 21 501-07, nr. 1750"),
            [KamerstukCitation("II", "2020/21", "21501-07", "1750")]
        )

        self.assertEqual(
            parse_kamerstukcitation("               90Kamerstukken II 2017/18, 21 501-07, nr. 1595"),
            [KamerstukCitation("II", "2017/18", "21501-07", "1595")]
        )

        self.assertEqual(
            parse_kamerstukcitation("               50Kamerstukken II 2015/16,  21 501-30, nr. 374"),
            [KamerstukCitation("II", "2015/16", "21501-30", "374")]
        )

    def test_citation_to_budget_law_dossier(self):
        """KamerstukCitation test for budgetarry laws dossiers, which have a particular dossiernumber of the form 35300-XV"""

        self.assertEqual(
            parse_kamerstukcitation("                  (Kamerstukken II 2019/20, 35 300-XV, nr. 28"),
            [KamerstukCitation("II", "2019/20", "35300-XV", "28")]
        )

        self.assertEqual(
            parse_kamerstukcitation("               2Kamerstukken II 2019/20, 35 300 XVI, nr. 133"),
            [KamerstukCitation("II", "2019/20", "35300-XVI", "133")]
        )
        self.assertEqual(
            parse_kamerstukcitation("               100Motie van het lid Sneller c.s., Kamerstukken II 2020/21 35 570-IX, nr. 14"),
            [KamerstukCitation("II", "2020/21", "35570-IX", "14")]
        )

    @unittest.skip("Rijksdossiernummers are currently not yet supported")
    def test_rijkswet_citation(self):
        """Test KamerstukCitation to a Rijkswet dossier, which has two dossier numbers, noted as e.g. 27 484 (R 1669)"""

        self.assertEqual(
            parse_kamerstukcitation("Ministerie van Binnenlandse Zaken en Koninkrijksrelaties (Kamerstukken I 2003/04, 27 484 (R 1669), nr. 289"),
            [KamerstukCitation("I", "2003/04", "27484", "289", rijksdossiernummer="R1669")]
        )

        self.assertEqual(
            parse_kamerstukcitation("               8Kamerstukken II 2015/16, 34 356 (R2064), nr. 3"),
            [KamerstukCitation("II", "2015/16", "34356", "3", rijksdossiernummer="R2064")]
        )

    def test_sloppy_citation(self):
        """KamerstukCitation test cases for citations that are not completely correct, but still contain all necessary information"""

        self.assertEqual(
            parse_kamerstukcitation("                  Studiegroep Begrotingsruimte)» bij Kamerstukken I 2020/21, 35 570, C; Kamerstukken II 2020/21, 35 570, nr. 3"),
            [KamerstukCitation("I", "2020/21", "35570", "C"), KamerstukCitation("II", "2020/21", "35570", "3")]
        )

    @unittest.skip("Multiple shorthand citations are currently not yet supported")
    def test_with_multiple_citations_shorthand(self):
        """KamerstukCitation: Multiple citations in a shorthand notation. Currently not supported."""

        self.assertEqual(
            parse_kamerstukcitation("               1Kamerstukken II 2020/21, 35 625, nr. 4, p. 12 en 13, en nr. 6"),
            [
                KamerstukCitation("II", "2020/21", "35625", "4", paginaverwijzing="p. 12 en 13"),
                KamerstukCitation("II", "2020/21", "35625", "6")
            ]
        )

        self.assertEqual(
            parse_kamerstukcitation("               15Kamerstukken II 2019/20, 29 754, nrs. 520 en 548 en Aanhangsel Handelingen II 2019/20, nr. 89"),
            [KamerstukCitation("II", "2019/20", "29754", "520"), KamerstukCitation("II", "2019/20", "29754", "548")]
        )

        self.assertEqual(
            parse_kamerstukcitation("""Een vordering tot tenuitvoerlegging slechts op grond van niet-naleving van een bijzondere
                                    voorwaarde kan ingevolge art. 14g, derde lid, Sr, evenals onder de voorheen geldende regeling,
                                    uitsluitend worden ingediend bij de rechter die de voorwaarde heeft opgelegd
                                     (Kamerstukken II, 1984–1985, 18764, nrs. 1–3, blz. 29). De wet voorziet niet in de mogelijkheid
                                     dat de behandeling van een zodanige vordering wordt gevoegd met de behandeling van een nieuwe
                                     strafzaak. Op een zodanige vordering dient derhalve een afzonderlijke beslissing te worden
                                     gegeven."""),
            [KamerstukCitation("II", "1984/1985", "18764", "1-3", paginaverwijzing="blz. 29")]
        )
