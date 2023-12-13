"""
    tests/test_ecli.py

    Test cases for citations to case law using ECLI's.

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

# pylint: disable=line-too-long, missing-function-docstring

import unittest

from nllegalcit import EcliCitation, parse_citations


class EcliCitationTests(unittest.TestCase):
    """Test cases for citations to case law using ECLI's"""

    def test_0(self):
        self.assertEqual(
            parse_citations("ECLI:NL:HR:2006:AV0653"),
            [EcliCitation("NL", "HR", 2006, "AV0653")]
        )
