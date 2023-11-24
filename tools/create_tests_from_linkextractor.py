#!/usr/bin/env python
"""
    tools/create_tests_from_linkextractor.py

    Automatically create python test cases from the linkextractor unit tests

    Copyright 2023, Martijn Staal <nllegalcit [at] martijn-staal.nl>

    Available under the EUPL-1.2, or, at your option, any later version.

    SPDX-License-Identifier: EUPL-1.2
"""

import argparse

import requests
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(
    prog="create_tests_from_linkextractor.py",
    description="Automatically create python test cases from the linkextractor unit tests",
    epilog="Copyright 2023, Martijn Staal, available under the EUPL-1.2 or later."
)

parser.add_argument("test", type=str, help="The linkextractor test to convert.")

args = parser.parse_args()

input_url = f"https://gitlab.com/koop/ld/lx/linkextractor/-/raw/main/src/webapp/links/test/input/{args.test}.txt?inline=false"
# unittest_url = f"https://gitlab.com/koop/ld/lx/linkextractor/-/raw/main/src/webapp/links/test/unit/{args.test}.xslt"

input_req = requests.get(input_url, timeout=30)

input = input_req.text

context = {
    "test": args.test,
    "testclassname": "GeneratedTestClass",
    "test_cases": []
}

for line in input.split('\n'):
    if line != '':
        test_case = {}
        test_case["name"] = f"test_{len(context['test_cases']) + 1}"
        test_case["input"] = line
        context["test_cases"].append(test_case)

jinja_env = Environment(loader=FileSystemLoader(searchpath="./"))
template = jinja_env.get_template("test_oebp.py.jinja2")

print(template.render(context))
