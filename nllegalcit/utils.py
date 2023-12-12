"""
    nllegalcit/utils.py

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

from lark import Tree, Token


def normalize_nl_ecli_court(court: str) -> str:
    """Normalize the formatting for Dutch ECLI court notations"""

    # TODO: There are definitely more cases to cover.
    if court.lower() == "rvs":
        return "RvS"
    if court.lower() == "hr":
        return "HR"

    return court


def lark_tree_to_str(tree: Tree) -> str:
    """Get the text that underlies a lark parse tree"""

    text = ""

    for c in tree.children:
        if isinstance(c, Token):
            text += str(c)
        elif isinstance(c, Tree):
            text += lark_tree_to_str(c)

    return text
