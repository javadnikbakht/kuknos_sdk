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

py-kuknos-sdk 是用于开发 Kuknos 应用程序的 Python 库。它目前支持 Python 3.6+ 和 PyPy3.6+。

它提供了：

- 完全访问 Horizon 各个接口的能力
- 快速的构建与签署事务，并将它提交到 Kuknos 网络

入门
----------
我强烈推荐你阅读官方的 `开发者文档 <https://www.kuknos.org/developers/guides/>`_ ，
其中介绍了诸多基础的概念，能帮助你快速的了解 Kuknos 网络中的各种概念。

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


API 文档
-----------------
Here you'll find detailed documentation on specific functions, classes, and
methods.

.. toctree::
   :maxdepth: 2

   api


资源
-----
* 文档: https://kuknos-sdk.readthedocs.io
* 源代码: https://github.com/javadnikbakht/py-kuknos-base/tree/v2
* Docker: https://hub.docker.com/r/overcat/py-kuknos-base
* 示例: https://github.com/javadnikbakht/py-kuknos-base/blob/v2/examples
* Issue 追踪: https://github.com/javadnikbakht/py-kuknos-base/issues
* 许可证: `Apache License 2.0 <https://github.com/javadnikbakht/py-kuknos-base/blob/master/LICENSE>`_
* 已发布版本: https://pypi.org/project/kuknos-sdk/

致谢
------
这份文档是在 `Kuknos JavaScript SDK`_ 文档的基础上完成的。在此感谢所有向 Kuknos 生态贡献过自己的一份力量的同学。


:ref:`genindex`
---------------


.. _here: https://github.com/javadnikbakht/py-kuknos-base/tree/master/examples
.. _Kuknos Horizon server: https://github.com/kuknos/go/tree/master/services/horizon
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _pipenv: https://github.com/pypa/pipenv
.. _Kuknos JavaScript SDK: https://www.kuknos.org/developers/js-kuknos-sdk/reference/
