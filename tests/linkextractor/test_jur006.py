"""
    tests/linkextractor/test-jur006.py

    Test cases for citations to Kamerstukken based on the linkextractor test-jur006.xslt test
    See:
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/unit/test-jur006.xslt
        - https://gitlab.com/koop/ld/lx/linkextractor/-/blob/main/src/webapp/links/test/input/test-jur006.txt

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit import EcliCitation, parse_citations


class GeneratedTestClass(unittest.TestCase):
    """Test cases for citations to Kamerstukken based on the linkextractor test-jur006.xslt test"""

    def test_2(self):
        self.assertEqual(
            parse_citations("ECLI:EU:C:1984:25"),
            [EcliCitation("EU", "C", 1984, "25")]
        )

    def test_3(self):
        self.assertEqual(
            parse_citations("EU:C:1984:25"),
            [EcliCitation("EU", "C", 1984, "25")]
        )

    def test_4(self):
        self.assertEqual(
            parse_citations("ECLI;EU;T;2015;314"),
            [EcliCitation("EU", "T", 2015, "314")]
        )

    def test_5(self):
        self.assertEqual(
            parse_citations("ECLI:DE:BVerwG:2014:041214B8B66.14.0"),
            [EcliCitation("DE", "BVerwG", 2014, "041214B8B66.14.0")]
        )

    def test_6(self):
        self.assertEqual(
            parse_citations("ECLI:FR:CCASS:2014:AV15001"),
            [EcliCitation("FR", "CCASS", 2014, "AV15001")]
        )

    def test_7(self):
        self.assertEqual(
            parse_citations("ECLI:SI:VSRS:2014:VIII.IPS.90.2014"),
            [EcliCitation("SI", "VSRS", 2014, "VIII.IPS.90.2014")]
        )

    def test_8(self):
        self.assertEqual(
            parse_citations("ECLI:SK:OSBA2:2012:1209219747.113"),
            [EcliCitation("SK", "OSBA2", 2012, "1209219747.113")]
        )

    def test_9(self):
        # Should be invalid
        self.assertEqual(
            parse_citations("ECLI:EU:C:1984:ab3254"),
            []
        )
