.. _install:

*****
安装
*****

通过 pipenv 或 pip 安装
=========================

通过 pipenv 来安装 Kuknos Python SDK ：

.. code-block:: text

    pipenv install kuknos-sdk==3.3.0

我们推荐你使用 `pipenv <https://docs.pipenv.org/>`_ 来安装这个模块。当然你也可以使用 `pip <https://pip.pypa.io/en/stable/quickstart/>`_。
想要更多的了解如何安装依赖，请参阅 `Hitchhiker's Guide to Python
<http://docs.python-guide.org/en/latest/starting/installation/>`_。

通过源码安装
============

请尽可能使用上述方法安装。最新的代码可能不稳定。

你可以先克隆 `这个仓库 <https://github.com/javadnikbakht/py-kuknos-base>`_，然后通过源码安装 SDK：

.. code-block:: bash

    git clone https://github.com/javadnikbakht/py-kuknos-base.git
    cd py-kuknos-base
    git checkout 3.3.0
    pip install .
