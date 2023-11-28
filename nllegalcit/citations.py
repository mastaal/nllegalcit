"""
    nllegalcit/citations.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

from enum import Enum
from typing import Optional


class Citation():
    """Generic citation"""


class KamerstukCitation(Citation):
    """Structured representation of a citation of a kamerstuk"""

    class Kamer(Enum):
        TK = "II"
        EK = "I"
        VV = "VV"

    kamer: Kamer
    vergaderjaar: str
    dossiernummer: str
    ondernummer: str
    paginaverwijzing: Optional[str]
    rijksdossiernummer: Optional[str]

    def __init__(
            self,
            kamer: str,
            vergaderjaar: str,
            dossiernummer: str,
            ondernummer: str,
            paginaverwijzing=None,
            rijksdossiernummer=None):
        self.kamer = kamer
        self.vergaderjaar = vergaderjaar
        self.dossiernummer = dossiernummer
        self.ondernummer = ondernummer
        self.paginaverwijzing = paginaverwijzing
        self.rijksdossiernummer = rijksdossiernummer

    def __str__(self) -> str:
        # There surely must be a better way to do this
        if self.rijksdossiernummer is not None and self.paginaverwijzing is not None:
            return (f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer}"
                    f" ({self.rijksdossiernummer}) {self.ondernummer} {self.paginaverwijzing}")
        if self.paginaverwijzing is not None:
            return (f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer}"
                    f"{self.ondernummer} {self.paginaverwijzing}")
        if self.rijksdossiernummer is not None:
            return (f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer}"
                    f" ({self.rijksdossiernummer}) {self.ondernummer}")

        return f"KamerstukCitation {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer}"

    def __repr__(self) -> str:
        if self.paginaverwijzing is not None:
            return f"Kamerstukken {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer} {self.paginaverwijzing}"

        return f"Kamerstukken {self.kamer} {self.vergaderjaar} {self.dossiernummer} {self.ondernummer}"

    def __eq__(self, other) -> bool:
        try:
            return ((self.kamer == other.kamer) and
                    (self.vergaderjaar == other.vergaderjaar) and
                    (self.dossiernummer == other.dossiernummer) and
                    (self.ondernummer == other.ondernummer) and
                    (self.paginaverwijzing == other.paginaverwijzing) and
                    (self.rijksdossiernummer == other.rijksdossiernummer))
        except AttributeError:
            return False
