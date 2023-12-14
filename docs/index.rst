.. nllegalcit documentation master file, created by
   sphinx-quickstart on Tue Nov 28 09:32:05 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to nllegalcit's documentation!
======================================

nllegalcit is a Python library to find citations to Dutch
legal and parliamentary documents in natural language text.

This library is partially based on the
`linkextractor <https://gitlab.com/koop/ld/lx/linkextractor>`_
developed by `KOOP <https://www.koopoverheid.nl/>`_ to implement
the Linked Data Overheid (LiDO). The aim of nllegalcit is to
provide a more generally accessible way to recognize Dutch legal
citations in natural language text.

**Please note that this library is currently under development.
It will probably not work reliably.**

Installation
------------

nllegalcit is currently built and tested for Python 3.10,
using either the default CPython or the (much faster) PyPy runtime.

nllegalcit can be installed using pip:

.. code:: bash

   $ pip install nllegalcit

Using nllegalcit
----------------

To find all supported citations in some string, we use the following general function:

.. autofunction:: nllegalcit.parse_citations

This gives us a list of all recognized citations in the input:
::

   >>> from nllegalcit import parse_citations
   >>> parse_citations("Kamerstukken I 1979/80, 15 516, nr. 42e, blz. 7")
   [Kamerstukken I 1979-1980, 15516, nr. 42e p. 7]

Other specific parse functions also exist, for example to find citations in a PDF file,
or to only find citations to Kamerstukken. For more information, please refer to :ref:`the API reference <nllegalcit_package>`.

Features
--------

nllegalcit aims to provide a simple interface to find all supported citations in a text. At its core,
nllegalcit consists of functions to parse a type of text (plaintext, PDF files, online PDF files, etc.),
and specific Citation classes to describe the recognized citations.

Only absolute citations are recognized. Detecting relative citations in a text is currently out of scope for
nllegalcit.

Supported citation types
------------------------
The following types of citations are implemented:

- Kamerstukken (Dutch parliamentary documents) [⚠️ Work in progress]:
   Works reasonably well for modern (>1995) citations following the guidelines. Older citations may work. Simple page number notations work.
- ECLI case law [⚠️ Work in progress]:
   Seems to work, but more testing is needed. Paragraph information is not parsed.

The following types of citations are not yet implemented, but are planned:

- Handelingen (Dutch parliamentary minutes)
- Dutch case law other than ECLI
- Dutch national laws
- Dutch treaties
- Dutch local laws
- EU laws

License and copyright
---------------------

Copyright (c) 2023 Martijn Staal <nllegalcit [a t ] martijn-staal.nl>

Available under the European Union Public License v1.2 (EUPL-1.2), or, at your option, any later version.

Issues
------

Please file any issues you may have in `GitHub <https://github.com/mastaal/nllegalcit/issues>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   performance.rst
   kamerstukken.rst
   caselaw.rst
   nllegalcit API reference <nllegalcit.rst>



Indices and tables
==================

* :ref:`genindex`
.. * :ref:`modindex`
* :ref:`search`
