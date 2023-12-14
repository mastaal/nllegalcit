# nllegalcit

[![GitHub License](https://img.shields.io/github/license/mastaal/nllegalcit?color=%23003399)](https://github.com/mastaal/nllegalcit/blob/main/LICENSE)
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/mastaal/nllegalcit/pytest.yml?label=tests)](https://github.com/mastaal/nllegalcit/actions/workflows/pytest.yml)
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/mastaal/nllegalcit/pylint.yml?label=linter)](https://github.com/mastaal/nllegalcit/actions/workflows/pylint.yml)
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/mastaal/nllegalcit/mypy.yml?label=type%20checking)](https://github.com/mastaal/nllegalcit/actions/workflows/mypy.yml)


A Python library to find citations to Dutch legal documents in natural language text.

This library is partially based on the [linkextractor](https://gitlab.com/koop/ld/lx/linkextractor) developed by [KOOP](https://www.koopoverheid.nl/) to implement the Linked Data Overheid (LiDO). The aim of `nllegalcit` is to provide a more generally accessible way to recognize Dutch legal citations in natural language text.

**Please note that this library is currently under development. It will probably not work reliably.**

## Supported citations

The following types of citations are implemented, work in progress, or planned:

| Citation type | Implementation status | Implementation notes |
|---------------|-----------------------|----------------------|
| Kamerstukken (Dutch parliamentary documents)  | ⚠️ Work in progress      | Works reasonably well for modern (>1995) citations following the guidelines. Older citations may work. Simple page number notations work. |
| Handelingen (Dutch parliamentary minutes)   | 🗓️ Planned               |
| ECLI case law citations  | ⚠️ Work in progress    | Seems to work, but more testing is needed. Paragraph information is not parsed. |
| Dutch case law other than ECLI | 🗓️ Planned |
| Dutch national laws | 🗓️ Planned |
| Dutch treaties | 🗓️ Planned |
| Dutch local law | 🗓️ Planned |
| EU law | 🗓️ Planned |

## License

Copyright (c) 2023 Martijn Staal <nllegalcit [a t ] martijn-staal.nl>

Available under the European Union Public License v1.2 (EUPL-1.2), or, at your option, any later version.
