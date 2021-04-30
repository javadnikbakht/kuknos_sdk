.. _create_account:


**************
Create Account
**************

Now, in order to create an account, you need to run a :py:class:`CreateAccount
<kuknos_sdk.operation.CreateAccount>` operation with your new account ID.
Due to `Kuknos's minimum account balance
<https://www.kuknos.org/developers/guides/concepts/fees.html#minimum-account-balance>`_,
you'll need to transfer the minimum account balance from another account with
the create account operation. As of this writing, minimum balance is **1 PMN (2
x 0.5 Base Reserve)**, and is subject to change.

Using The SDF Testnet
=====================
If you want to play in the Kuknos test network, you can ask our `Friendbot
<https://www.kuknos.org/developers/guides/get-started/create-account.html>`_
to create an account for you as shown below:

.. literalinclude:: ../../examples/create_account_friendbot.py
   :language: python
   :linenos:

Using The Kuknos Live Network
==============================
On the other hand, if you would like to create an account on the live network,
you should buy some Kuknos Paymons from an exchange. When you withdraw the
Paymons into your new account, the exchange will automatically create the
account for you. However, if you want to create an account from another
account of your own, here's an example of how to do so:


.. literalinclude:: ../../examples/create_account.py
   :language: python
   :linenos:
