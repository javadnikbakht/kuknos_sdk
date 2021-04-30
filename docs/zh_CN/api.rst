.. _api:

*****************
API 文档
*****************


.. module:: kuknos_sdk


Account
^^^^^^^^

.. autoclass:: kuknos_sdk.account.Account
   :members:
   :inherited-members:

Asset
^^^^^

.. autoclass:: kuknos_sdk.asset.Asset
   :members:
   :inherited-members:

Call Builder
^^^^^^^^^^^^

BaseCallBuilder
-------------------
.. autoclass:: kuknos_sdk.call_builder.BaseCallBuilder
   :members:
   :inherited-members:

AccountsCallBuilder
-------------------
.. autoclass:: kuknos_sdk.call_builder.AccountsCallBuilder
   :members:
   :inherited-members:

AssetsCallBuilder
-----------------
.. autoclass:: kuknos_sdk.call_builder.AssetsCallBuilder
   :members:
   :inherited-members:

ClaimableBalancesCallBuilder
---------------------------
.. autoclass:: kuknos_sdk.call_builder.ClaimableBalancesCallBuilder
   :members:
   :inherited-members:

DataCallBuilder
---------------
.. autoclass:: kuknos_sdk.call_builder.DataCallBuilder
   :members:
   :inherited-members:

EffectsCallBuilder
------------------
.. autoclass:: kuknos_sdk.call_builder.EffectsCallBuilder
   :members:
   :inherited-members:

FeeStatsCallBuilder
-------------------
.. autoclass:: kuknos_sdk.call_builder.FeeStatsCallBuilder
   :members:
   :inherited-members:

LedgersCallBuilder
------------------
.. autoclass:: kuknos_sdk.call_builder.LedgersCallBuilder
   :members:
   :inherited-members:

OffersCallBuilder
---------------------
.. autoclass:: kuknos_sdk.call_builder.OffersCallBuilder
   :members:
   :inherited-members:

OperationsCallBuilder
---------------------
.. autoclass:: kuknos_sdk.call_builder.OperationsCallBuilder
   :members:
   :inherited-members:

OrderbookCallBuilder
--------------------
.. autoclass:: kuknos_sdk.call_builder.OrderbookCallBuilder
   :members:
   :inherited-members:

PaymentsCallBuilder
-------------------
.. autoclass:: kuknos_sdk.call_builder.PaymentsCallBuilder
   :members:
   :inherited-members:

RootCallBuilder
-------------------
.. autoclass:: kuknos_sdk.call_builder.RootCallBuilder
   :members:
   :inherited-members:

StrictReceivePathsCallBuilder
------------------------------
.. autoclass:: kuknos_sdk.call_builder.StrictReceivePathsCallBuilder
   :members:
   :inherited-members:

StrictSendPathsCallBuilder
------------------------------
.. autoclass:: kuknos_sdk.call_builder.StrictSendPathsCallBuilder
   :members:
   :inherited-members:

TradeAggregationsCallBuilder
----------------------------
.. autoclass:: kuknos_sdk.call_builder.TradeAggregationsCallBuilder
   :members:
   :inherited-members:

TradesCallBuilder
-----------------
.. autoclass:: kuknos_sdk.call_builder.TradesCallBuilder
   :members:
   :inherited-members:

TransactionsCallBuilder
-----------------------
.. autoclass:: kuknos_sdk.call_builder.TransactionsCallBuilder
   :members:
   :inherited-members:

Client
^^^^^^

BaseAsyncClient
---------------

.. autoclass:: kuknos_sdk.client.base_async_client.BaseAsyncClient
   :members:

BaseSyncClient
---------------

.. autoclass:: kuknos_sdk.client.base_sync_client.BaseSyncClient
   :members:

AiohttpClient
--------------

.. autoclass:: kuknos_sdk.client.aiohttp_client.AiohttpClient
   :members:

RequestsClient
--------------

.. autoclass:: kuknos_sdk.client.requests_client.RequestsClient
   :members:

SimpleRequestsClient
--------------------

.. autoclass:: kuknos_sdk.client.simple_requests_client.SimpleRequestsClient
   :members:

Response
--------

.. autoclass:: kuknos_sdk.client.response.Response
   :members:



Exceptions
^^^^^^^^^^

SdkError
--------

.. autoclass:: kuknos_sdk.exceptions.SdkError
   :members:

ValueError
----------

.. autoclass:: kuknos_sdk.exceptions.ValueError
   :members:

TypeError
---------

.. autoclass:: kuknos_sdk.exceptions.TypeError
   :members:

BadSignatureError
-----------------

.. autoclass:: kuknos_sdk.exceptions.BadSignatureError
   :members:

Ed25519PublicKeyInvalidError
----------------------------

.. autoclass:: kuknos_sdk.exceptions.Ed25519PublicKeyInvalidError
   :members:

Ed25519SecretSeedInvalidError
-----------------------------

.. autoclass:: kuknos_sdk.exceptions.Ed25519SecretSeedInvalidError
   :members:

MissingEd25519SecretSeedError
-----------------------------

.. autoclass:: kuknos_sdk.exceptions.MissingEd25519SecretSeedError
   :members:

MemoInvalidException
--------------------

.. autoclass:: kuknos_sdk.exceptions.MemoInvalidException
   :members:

AssetCodeInvalidError
---------------------

.. autoclass:: kuknos_sdk.exceptions.AssetCodeInvalidError
   :members:

AssetIssuerInvalidError
-----------------------

.. autoclass:: kuknos_sdk.exceptions.AssetIssuerInvalidError
   :members:

NoApproximationError
--------------------

.. autoclass:: kuknos_sdk.exceptions.NoApproximationError
   :members:

SignatureExistError
-------------------

.. autoclass:: kuknos_sdk.exceptions.SignatureExistError
   :members:

BaseRequestError
----------------

.. autoclass:: kuknos_sdk.exceptions.BaseRequestError
   :members:

ConnectionError
---------------

.. autoclass:: kuknos_sdk.exceptions.ConnectionError
   :members:

BaseHorizonError
----------------

.. autoclass:: kuknos_sdk.exceptions.BaseHorizonError
   :members:

NotFoundError
-------------

.. autoclass:: kuknos_sdk.exceptions.NotFoundError
   :members:

BadRequestError
---------------

.. autoclass:: kuknos_sdk.exceptions.BadRequestError
   :members:

BadResponseError
----------------

.. autoclass:: kuknos_sdk.exceptions.BadResponseError
   :members:

Keypair
^^^^^^^

.. autoclass:: kuknos_sdk.keypair.Keypair
   :members:
   :inherited-members:

Memo
^^^^

Memo
----

.. autoclass:: kuknos_sdk.memo.Memo
   :members:

NoneMemo
--------
.. autoclass:: kuknos_sdk.memo.NoneMemo
   :members:

TextMemo
--------
.. autoclass:: kuknos_sdk.memo.TextMemo
   :members:

IdMemo
------
.. autoclass:: kuknos_sdk.memo.IdMemo
   :members:

HashMemo
--------
.. autoclass:: kuknos_sdk.memo.HashMemo
   :members:

ReturnHashMemo
--------------
.. autoclass:: kuknos_sdk.memo.ReturnHashMemo
   :members:

Network
^^^^^^^

.. autoclass:: kuknos_sdk.network.Network
   :members:
   :inherited-members:

.. _operation_list_archor:

Operation
^^^^^^^^^

Operation
---------
.. autoclass:: kuknos_sdk.operation.Operation
   :members:
   :inherited-members:

OperationType
-------------
.. autoclass:: kuknos_sdk.operation.operation_type.OperationType
   :members:

AccountMerge
------------
.. autoclass:: kuknos_sdk.operation.AccountMerge
   :members: to_xdr_object, from_xdr_object

AllowTrust
----------
.. autoclass:: kuknos_sdk.operation.AllowTrust
   :members: to_xdr_object, from_xdr_object

.. autoclass:: kuknos_sdk.operation.allow_trust.TrustLineEntryFlag
   :members:

BumpSequence
------------
.. autoclass:: kuknos_sdk.operation.BumpSequence
   :members: to_xdr_object, from_xdr_object

ChangeTrust
-----------
.. autoclass:: kuknos_sdk.operation.ChangeTrust
   :members: to_xdr_object, from_xdr_object

CreateAccount
-------------
.. autoclass:: kuknos_sdk.operation.CreateAccount
   :members: to_xdr_object, from_xdr_object

CreatePassiveSellOffer
----------------------
.. autoclass:: kuknos_sdk.operation.CreatePassiveSellOffer
   :members: to_xdr_object, from_xdr_object

Inflation
---------
.. autoclass:: kuknos_sdk.operation.Inflation
   :members: to_xdr_object, from_xdr_object

ManageBuyOffer
--------------
.. autoclass:: kuknos_sdk.operation.ManageBuyOffer
   :members: to_xdr_object, from_xdr_object

ManageData
----------
.. autoclass:: kuknos_sdk.operation.ManageData
   :members: to_xdr_object, from_xdr_object

ManageSellOffer
---------------
.. autoclass:: kuknos_sdk.operation.ManageSellOffer
   :members: to_xdr_object, from_xdr_object

PathPayment
-----------
.. autoclass:: kuknos_sdk.operation.PathPayment
   :members: to_xdr_object, from_xdr_object

PathPaymentStrictReceive
------------------------
.. autoclass:: kuknos_sdk.operation.PathPaymentStrictReceive
   :members: to_xdr_object, from_xdr_object

PathPaymentStrictSend
---------------------
.. autoclass:: kuknos_sdk.operation.PathPaymentStrictSend
   :members: to_xdr_object, from_xdr_object

Payment
-------
.. autoclass:: kuknos_sdk.operation.Payment
   :members: to_xdr_object, from_xdr_object

SetOptions
----------
.. autoclass:: kuknos_sdk.operation.SetOptions
   :members: to_xdr_object, from_xdr_object

.. autoclass:: kuknos_sdk.operation.set_options.AuthorizationFlag
   :members:

CreateClaimableBalance
----------------------
.. autoclass:: kuknos_sdk.operation.CreateClaimableBalance
   :members: to_xdr_object, from_xdr_object

.. autoclass:: kuknos_sdk.operation.Claimant
   :members:

.. autoclass:: kuknos_sdk.operation.ClaimPredicate
   :members:

.. autoclass:: kuknos_sdk.operation.create_claimable_balance.ClaimPredicateType
   :members:

.. autoclass:: kuknos_sdk.operation.create_claimable_balance.ClaimPredicateGroup
   :members:

ClaimClaimableBalance
---------------------
.. autoclass:: kuknos_sdk.operation.ClaimClaimableBalance
   :members: to_xdr_object, from_xdr_object

BeginSponsoringFutureReserves
-----------------------------
.. autoclass:: kuknos_sdk.operation.BeginSponsoringFutureReserves
   :members: to_xdr_object, from_xdr_object

EndSponsoringFutureReserves
---------------------------
.. autoclass:: kuknos_sdk.operation.EndSponsoringFutureReserves
   :members: to_xdr_object, from_xdr_object

RevokeSponsorship
-----------------
.. autoclass:: kuknos_sdk.operation.RevokeSponsorship
   :members: to_xdr_object, from_xdr_object

.. autoclass:: kuknos_sdk.operation.revoke_sponsorship.RevokeSponsorshipType
   :members:

.. autoclass:: kuknos_sdk.operation.revoke_sponsorship.TrustLine
   :members:

.. autoclass:: kuknos_sdk.operation.revoke_sponsorship.Offer
   :members:

.. autoclass:: kuknos_sdk.operation.revoke_sponsorship.Data
   :members:

.. autoclass:: kuknos_sdk.operation.revoke_sponsorship.Signer
   :members:

Clawback
--------
.. autoclass:: kuknos_sdk.operation.Clawback
   :members: to_xdr_object, from_xdr_object

ClawbackClaimableBalance
------------------------
.. autoclass:: kuknos_sdk.operation.ClawbackClaimableBalance
   :members: to_xdr_object, from_xdr_object

SetTrustLineFlags
-----------------
.. autoclass:: kuknos_sdk.operation.SetTrustLineFlags
   :members: to_xdr_object, from_xdr_object

.. autoclass:: kuknos_sdk.operation.set_trust_line_flags.TrustLineFlags
   :members:

Price
^^^^^

.. autoclass:: kuknos_sdk.price.Price
   :members:
   :inherited-members:

Server
^^^^^^

.. autoclass:: kuknos_sdk.server.Server
   :members:
   :inherited-members:

Signer
^^^^^^

.. autoclass:: kuknos_sdk.signer.Signer
   :members:
   :inherited-members:

SignerKey
^^^^^^^^^

.. autoclass:: kuknos_sdk.signer_key.SignerKey
   :members:
   :inherited-members:

TimeBounds
^^^^^^^^^^

.. autoclass:: kuknos_sdk.time_bounds.TimeBounds
   :members:
   :inherited-members:

Transaction
^^^^^^^^^^^

.. autoclass:: kuknos_sdk.transaction.Transaction
   :members:

TransactionEnvelope
^^^^^^^^^^^^^^^^^^^

.. autoclass:: kuknos_sdk.transaction_envelope.TransactionEnvelope
   :members:
   :inherited-members:

FeeBumpTransaction
^^^^^^^^^^^^^^^^^^

.. autoclass:: kuknos_sdk.fee_bump_transaction.FeeBumpTransaction
   :members:
   :inherited-members:

FeeBumpTransactionEnvelope
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: kuknos_sdk.fee_bump_transaction_envelope.FeeBumpTransactionEnvelope
   :members:
   :inherited-members:

TransactionBuilder
^^^^^^^^^^^^^^^^^^

.. autoclass:: kuknos_sdk.transaction_builder.TransactionBuilder
   :members:

Helpers
^^^^^^^
.. autofunction:: kuknos_sdk.helpers.parse_transaction_envelope_from_xdr

XDR Utils
^^^^^^^^^
.. autofunction:: kuknos_sdk.xdr.utils.from_xdr_amount
.. autofunction:: kuknos_sdk.xdr.utils.to_xdr_amount

Kuknos Ecosystem Proposals
^^^^^^^^^^^^^^^^^^^^^^^^^^^
SEP 0001: kuknos.toml
----------------------
.. autofunction:: kuknos_sdk.sep.kuknos_toml.fetch_kuknos_toml

SEP 0002: Federation protocol
-----------------------------
.. autofunction:: kuknos_sdk.sep.federation.resolve_kuknos_address
.. autofunction:: kuknos_sdk.sep.federation.resolve_account_id
.. autoclass:: kuknos_sdk.sep.federation.FederationRecord
   :members:

SEP 0005: Key Derivation Methods for Kuknos Accounts
-----------------------------------------------------
.. autoclass:: kuknos_sdk.sep.mnemonic.KuknosMnemonic
   :members:
.. autoclass:: kuknos_sdk.sep.mnemonic.Language
   :members:
   :undoc-members:

SEP 0007: URI Scheme to facilitate delegated signing
-----------------------------------------------------
.. autoclass:: kuknos_sdk.sep.kuknos_uri.PayKuknosUri
   :members:
   :inherited-members:
.. autoclass:: kuknos_sdk.sep.kuknos_uri.TransactionKuknosUri
   :members:
   :inherited-members:
.. autoclass:: kuknos_sdk.sep.kuknos_uri.Replacement
   :members:
   :inherited-members:

SEP 0010: Kuknos Web Authentication
------------------------------------
.. autofunction:: kuknos_sdk.sep.kuknos_web_authentication.build_challenge_transaction
.. autofunction:: kuknos_sdk.sep.kuknos_web_authentication.read_challenge_transaction
.. autofunction:: kuknos_sdk.sep.kuknos_web_authentication.verify_challenge_transaction_threshold
.. autofunction:: kuknos_sdk.sep.kuknos_web_authentication.verify_challenge_transaction_signed_by_client_master_key
.. autofunction:: kuknos_sdk.sep.kuknos_web_authentication.verify_challenge_transaction_signers
.. autofunction:: kuknos_sdk.sep.kuknos_web_authentication.verify_challenge_transaction

SEP 0011: Txrep: human-readable low-level representation of Kuknos transactions
---------------------------------------------------------------------------------
.. autofunction:: kuknos_sdk.sep.txrep.to_txrep
.. autofunction:: kuknos_sdk.sep.txrep.from_txrep

Exceptions
----------
.. autoclass:: kuknos_sdk.sep.exceptions.KuknosTomlNotFoundError
.. autoclass:: kuknos_sdk.sep.exceptions.InvalidFederationAddress
.. autoclass:: kuknos_sdk.sep.exceptions.FederationServerNotFoundError
.. autoclass:: kuknos_sdk.sep.exceptions.BadFederationResponseError
.. autoclass:: kuknos_sdk.sep.exceptions.InvalidSep10ChallengeError
.. autoclass:: kuknos_sdk.sep.exceptions.AccountRequiresMemoError