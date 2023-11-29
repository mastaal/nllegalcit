.. nllegalcit documentation master file, created by
   sphinx-quickstart on Tue Nov 28 09:32:05 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to nllegalcit's documentation!
======================================

nllegalcit is a Python (>=3.10) library to find citations to Dutch
legal and parliamentary documents in natural language text.

This library is partially based on the
`linkextractor <https://gitlab.com/koop/ld/lx/linkextractor>`_
developed by `KOOP <https://www.koopoverheid.nl/>`_ to implement
the Linked Data Overheid (LiDO). The aim of nllegalcit is to
provide a more generally accessible way to recognize Dutch legal
citations in natural language text.

**Please note that this library is currently under development.
It will probably not work reliably.**

Supported citation types
------------------------

The following types of citations are implemented, work in progress, or planned:

.. csv-table::
   :header: Citation type, Implementation status, Implementation notes

   "Kamerstukken (Dutch parliamentary documents)", "⚠️ Work in progress", "Works reasonably well for modern (>1995) citations following the guidelines. Older citations may work. Page number recognition is unreliable."
   "Handelingen (Dutch parliamentary minutes)", "🗓️ Planned", ""
   "ECLI case law citations", "⚠️ Work in progress", "Tested to work outside of other textual context. Paragraph information is not parsed."
   "Dutch case law other than ECLI", "🗓️ Planned", ""
   "Dutch national laws", "🗓️ Planned", ""
   "Dutch treaties", "🗓️ Planned", ""
   "Dutch local laws", "🗓️ Planned", ""
   "EU laws", "🗓️ Planned", ""

General usage
-------------

To find all supported citations in some string, we use the following general function:

.. autofunction:: nllegalcit.parser.parse_citations

This gives us a list of all recognized citations in the input:
::

   >>> from nllegalcit.parser import parse_citations
   >>> parse_citations("Kamerstukken I 1979/80, 15 516, nr. 42e, blz. 7")
   [Kamerstukken I 1979-1980, 15516, nr. 42e p. 7]

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   kamerstukken.rst
   caselaw.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
