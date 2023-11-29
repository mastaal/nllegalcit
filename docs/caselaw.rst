Case law
========

nllegalcit supports citations to case law. Currently, only citations using an `European Case Law Identifier (ECLI) <https://en.wikipedia.org/wiki/European_Case_Law_Identifier>`_
are supported. Although it should generally work for all ECLI's, the current implementation is heavily
geared towards citations for Dutch case law.

Paragraph information from citations is currently not yet parsed.

.. autoclass:: nllegalcit.citations.CaseLawCitation


ECLI-based case law citations
-----------------------------

For ECLI-based case law citations, the current implementation is lax for Dutch citations, allowing the ommission of both the 'ECLI:' prefix and the country code 'NL'. For citations to ECHR case law, the 'ECLI:CE' part may also be ommitted. For EU case law, only the 'ECLI' part may be ommitted.

For other case law citations, nllegalcit will only recognize them if they are strictly according to the ECLI standard.

.. autoclass:: nllegalcit.citations.EcliCitation