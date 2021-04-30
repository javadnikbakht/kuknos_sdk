.. _create_account:


**************
创建账户
**************

你需要通过 :py:class:`CreateAccount
<kuknos_sdk.operation.CreateAccount>` 操作来创建 Kuknos 中的账户。
由于 `恒星网络对账户有着最低持币要求
<https://www.kuknos.org/developers/guides/concepts/fees.html#minimum-account-balance>`_,
所以你需要给待激活账户发送一定数量的 PMN。当前这个数量是 **1 PMN (2
x 0.5 Base Reserve)**，它可能会变化，但是通常很长时间才会变动一次，所以你可以将它视为一个固定值。

使用测试网络
=====================
如果你想在测试网络中进行测试，你可以通过 `Friendbot
<https://www.kuknos.org/developers/guides/get-started/create-account.html>`_
来激活你的帐号。

.. literalinclude:: ../../examples/create_account_friendbot.py
   :language: python
   :linenos:

使用公共网络
==============================
如果你想在公共网络中创建一个账户的话，你可以让你的朋友给你发送一些 PMN，也可以在交易所购买一些，
当你从交易所提取 PMN 到一个新账户时，交易所一般会帮你创建好这个账户。如果你想使用你的账户创建另外一个账户的话，可以参考下面的代码。

.. literalinclude:: ../../examples/create_account.py
   :language: python
   :linenos: