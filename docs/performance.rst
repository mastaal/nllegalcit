Performance
===========

The performance of nllegalcit is heavily dependent on the performance of
the underlying parsing library, Lark. In general, the runtime of nllegalcit
can be greatly improved by using the `PyPy <https://www.pypy.org/>`_ runtime 
instead of the default CPython Python implementation. For example, running
all the nllegalcit tests is about 2.8 times faster using PyPy.