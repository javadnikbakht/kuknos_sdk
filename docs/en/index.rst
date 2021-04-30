.. py-kuknos-sdk documentation master file, created by
   sphinx-quickstart on Sat Jan 20 11:58:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. .. include:: ../README.rst

Kuknos Python SDK
==================

.. image:: https://img.shields.io/travis/javadnikbakht/py-kuknos-base/v2?style=flat-square&maxAge=1800
    :alt: Travis (.org)
    :target: https://travis-ci.org/javadnikbakht/py-kuknos-base/

.. image:: https://img.shields.io/readthedocs/kuknos-sdk.svg?style=flat-square&maxAge=1800
    :alt: Read the Docs
    :target: https://kuknos-sdk.readthedocs.io/en/latest/

.. image:: https://img.shields.io/codecov/c/github/javadnikbakht/py-kuknos-base/v2?style=flat-square&maxAge=1800
    :alt: Codecov
    :target: https://codecov.io/gh/javadnikbakht/py-kuknos-base

.. image:: https://img.shields.io/codeclimate/maintainability/javadnikbakht/py-kuknos-base?style=flat-square&maxAge=1800
    :alt: Code Climate maintainability
    :target: https://codeclimate.com/github/javadnikbakht/py-kuknos-base/maintainability

.. image:: https://img.shields.io/pypi/v/kuknos-sdk.svg?style=flat-square&maxAge=1800
    :alt: PyPI
    :target: https://pypi.python.org/pypi/kuknos-sdk

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue?style=flat-square
    :alt: Python - Version
    :target: https://pypi.python.org/pypi/kuknos-sdk

.. image:: https://img.shields.io/badge/implementation-cpython%20%7C%20pypy-blue?style=flat-square
    :alt: PyPI - Implementation
    :target: https://pypi.python.org/pypi/kuknos-sdk

py-kuknos-sdk is a Python library for communicating with
a `Kuknos Horizon server`_. It is used for building Kuknos apps on Python. It supports **Python 3.6+** as
well as PyPy 3.6+.

It provides:

- a networking layer API for Horizon endpoints.
- facilities for building and signing transactions, for communicating with a Kuknos Horizon instance, and for submitting transactions or querying network history.

Quickstart
----------
At the absolute basics, you'll want to read up on `Kuknos's Documentation
Guides <https://www.kuknos.org/developers/guides/>`_, as it contains a lot of
information on the concepts used below (Transactions, Payments, Operations,
KeyPairs, etc.).

.. toctree::
   :maxdepth: 2

   install
   generate_keypair
   create_account
   querying_horizon
   assets
   building_transactions
   payment
   asynchronous
   multi_signature_account


API Documentation
-----------------
Here you'll find detailed documentation on specific functions, classes, and
methods.

.. toctree::
   :maxdepth: 2

   api


Links
-----
* Document: https://kuknos-sdk.readthedocs.io
* Code: https://github.com/javadnikbakht/py-kuknos-base/tree/v2
* Docker: https://hub.docker.com/r/overcat/py-kuknos-base
* Examples: https://github.com/javadnikbakht/py-kuknos-base/blob/v2/examples
* Issue tracker: https://github.com/javadnikbakht/py-kuknos-base/issues
* License: `Apache License 2.0 <https://github.com/javadnikbakht/py-kuknos-base/blob/master/LICENSE>`_
* Releases: https://pypi.org/project/kuknos-sdk/

Thanks
------
This document is based on `Kuknos JavaScript SDK`_ documentation.
Thank you to all the people who have already contributed to Kuknos ecosystem!


:ref:`genindex`
---------------


.. _here: https://github.com/javadnikbakht/py-kuknos-base/tree/master/examples
.. _Kuknos Horizon server: https://github.com/kuknos/go/tree/master/services/horizon
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _pipenv: https://github.com/pypa/pipenv
.. _Kuknos JavaScript SDK: https://www.kuknos.org/developers/js-kuknos-sdk/reference/
