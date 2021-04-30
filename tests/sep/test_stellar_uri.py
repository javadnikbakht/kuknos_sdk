import pytest

from kuknos_sdk import Keypair, Asset, Network
from kuknos_sdk.exceptions import ValueError
from kuknos_sdk.memo import *
from kuknos_sdk.sep.kuknos_uri import (
    PayKuknosUri,
    TransactionKuknosUri,
    Replacement,
)
from kuknos_sdk.transaction_envelope import TransactionEnvelope
from kuknos_sdk.fee_bump_transaction_envelope import FeeBumpTransactionEnvelope


class TestKuknosTransactionKuknosUri:
    xdr = "AAAAAP+yw+ZEuNg533pUmwlYxfrq6/BoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH//////////AAAAAAAAAAA="
    tx = TransactionEnvelope.from_xdr(xdr, Network.TESTNET_NETWORK_PASSPHRASE)

    fee_bump_tx_xdr = "AAAABQAAAABDqliFalCjYChydhLNq0lXO8PWMJGrsl8naSePTpNR2wAAAAAAAAGQAAAAAgAAAABzdv3ojkzWHMD7KUoXhrPx0GH18vHKV0ZfqpMiEblG1gAAADIAAAAAAAAwOgAAAAAAAAAAAAAAAQAAAAAAAAABAAAAAGqka26GRAaOmdSR+9P28gWFYn/iQ3GPQsRGAuT5bF4JAAAAAAAAAAA7msoAAAAAAAAAAAERuUbWAAAAQM7EA7Pnkeyqzpa+KgOTDLX66WKBk32BSF4NocSAeOkfUDwIODWvgcToOAH4+jaeOqdWhmxjC0mQ0vO3V14u7AwAAAAAAAAAAU6TUdsAAABAt2wuZNUirKyCkv7Sc3B1kk5CUPt7eitpaZjRBpbrW1p8wVIZ6IsaRzzIVHP7YpGhzbPImXkahlolf0IL3sevBA=="
    fee_bump_tx = FeeBumpTransactionEnvelope.from_xdr(
        fee_bump_tx_xdr, Network.TESTNET_NETWORK_PASSPHRASE
    )

    @pytest.mark.parametrize(
        "tx, replace, callback, pubkey, message, network_passphrase, origin_domain, signature, signer, uri",
        [
            (
                tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    )
                ],
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline",
            ),
            (
                tx,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D",
            ),
            (
                tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    ),
                    Replacement("seqNum", "Y", "sequence for sourceAccount"),
                ],
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&replace=sourceAccount%3AX%2CseqNum%3AY%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline%2CY%3Asequence%20for%20sourceAccount",
            ),
            (
                tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    )
                ],
                None,
                None,
                None,
                None,
                None,
                None,
                "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC",
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&signature=VES7qVW1mbxV7PFDi8DvyrxP2EUhYqqGnw%2B%2BQEeIZeYIlrdvc9qqQo0dqtOR4qb2npoml1rlp%2F30WPikSaE6Bg%3D%3D",
            ),
            (
                tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    )
                ],
                None,
                None,
                None,
                None,
                None,
                "testSignature",
                "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC",
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&signature=VES7qVW1mbxV7PFDi8DvyrxP2EUhYqqGnw%2B%2BQEeIZeYIlrdvc9qqQo0dqtOR4qb2npoml1rlp%2F30WPikSaE6Bg%3D%3D",
            ),
            (
                tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    )
                ],
                None,
                None,
                None,
                None,
                None,
                "testSignature",
                None,
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&signature=testSignature",
            ),
            (
                tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    )
                ],
                None,
                None,
                None,
                None,
                None,
                None,
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&signature=VES7qVW1mbxV7PFDi8DvyrxP2EUhYqqGnw%2B%2BQEeIZeYIlrdvc9qqQo0dqtOR4qb2npoml1rlp%2F30WPikSaE6Bg%3D%3D",
            ),
            (
                tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    )
                ],
                "https://someSigningService.com",
                "GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS",
                "a" * 300,
                Network.TESTNET_NETWORK_PASSPHRASE,
                "someDomain.com",
                "testSignature",
                "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC",
                "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&callback=url%3Ahttps%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D",
            ),
            (
                fee_bump_tx,
                [
                    Replacement(
                        "sourceAccount", "X", "account on which to create the trustline"
                    )
                ],
                "https://someSigningService.com",
                "GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS",
                "a" * 300,
                Network.TESTNET_NETWORK_PASSPHRASE,
                "someDomain.com",
                "testSignature",
                "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC",
                "web+kuknos:tx?xdr=AAAABQAAAABDqliFalCjYChydhLNq0lXO8PWMJGrsl8naSePTpNR2wAAAAAAAAGQAAAAAgAAAABzdv3ojkzWHMD7KUoXhrPx0GH18vHKV0ZfqpMiEblG1gAAADIAAAAAAAAwOgAAAAAAAAAAAAAAAQAAAAAAAAABAAAAAGqka26GRAaOmdSR%2B9P28gWFYn%2FiQ3GPQsRGAuT5bF4JAAAAAAAAAAA7msoAAAAAAAAAAAERuUbWAAAAQM7EA7Pnkeyqzpa%2BKgOTDLX66WKBk32BSF4NocSAeOkfUDwIODWvgcToOAH4%2BjaeOqdWhmxjC0mQ0vO3V14u7AwAAAAAAAAAAU6TUdsAAABAt2wuZNUirKyCkv7Sc3B1kk5CUPt7eitpaZjRBpbrW1p8wVIZ6IsaRzzIVHP7YpGhzbPImXkahlolf0IL3sevBA%3D%3D&callback=url%3Ahttps%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=x968yy0d2uFhx6At2mxd6yK%2F0ZZCz%2F%2FQT%2BmlIXmJwI6xe4RuYVIPZpROVx8HUYtcL9ok%2FrwzlQHnBg%2F%2Ba0YYDg%3D%3D",
            ),
        ],
    )
    def test_to_uri(
        self,
        tx,
        replace,
        callback,
        pubkey,
        message,
        network_passphrase,
        origin_domain,
        signature,
        signer,
        uri,
    ):
        uri_builder = TransactionKuknosUri(
            transaction_envelope=tx,
            replace=replace,
            callback=callback,
            pubkey=pubkey,
            message=message,
            network_passphrase=network_passphrase,
            origin_domain=origin_domain,
            signature=signature,
        )
        if signer:
            uri_builder.sign(signer)
        assert uri_builder.to_uri() == uri
        restore_uri = TransactionKuknosUri.from_uri(
            uri_builder.to_uri(), Network.TESTNET_NETWORK_PASSPHRASE
        ).to_uri()
        if network_passphrase is None:
            restore_uri = restore_uri.replace(
                "&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015", ""
            )
        assert restore_uri == uri

    def test_message_too_long_raise(self):
        message = "_" * 301
        with pytest.raises(ValueError, match="Message must not exceed 300 characters."):
            TransactionKuknosUri(
                transaction_envelope=self.tx, message=message,
            )

    def test_equal(self):
        assert TransactionKuknosUri(
            transaction_envelope=self.tx
        ) == TransactionKuknosUri(transaction_envelope=self.tx)

    def test_invalid_callback_raise(self):
        uri = "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&callback=https%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D"
        with pytest.raises(ValueError, match="`callback` should start with `url:`."):
            TransactionKuknosUri.from_uri(uri, Network.TESTNET_NETWORK_PASSPHRASE)

    def test_missing_network_passphrase_raise(self):
        uri = "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&callback=https%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D"
        with pytest.raises(ValueError, match="`network_passphrase` is required."):
            TransactionKuknosUri.from_uri(uri, None)

    def test_invalid_scheme_raise(self):
        uri = "invalid+web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&callback=url%3Ahttps%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D"
        # TODO: recheck: Kuknos URI scheme should be `web+kuknos`, but got `invalid+web+kuknos`.
        with pytest.raises(ValueError, match="Kuknos URI scheme should be"):
            TransactionKuknosUri.from_uri(uri, Network.TESTNET_NETWORK_PASSPHRASE)

    def test_invalid_path_raise(self):
        uri = "web+kuknos:invalid_tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&callback=url%3Ahttps%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D"
        with pytest.raises(
            ValueError, match="Kuknos URI path should be `tx`, but got `invalid_tx`."
        ):
            TransactionKuknosUri.from_uri(uri, Network.TESTNET_NETWORK_PASSPHRASE)

    # TODO: add more tests
    def test_invalid_replace_raise(self):
        uri = "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&callback=url%3Ahttps%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BY%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D"
        with pytest.raises(ValueError, match="Invalid `replace`."):
            TransactionKuknosUri.from_uri(uri, Network.TESTNET_NETWORK_PASSPHRASE)

    def test_missing_xdr_passphrase_raise(self):
        uri = "web+kuknos:tx?callback=url%3Ahttps%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D"
        with pytest.raises(ValueError, match="`xdr` is missing from uri."):
            TransactionKuknosUri.from_uri(uri, Network.TESTNET_NETWORK_PASSPHRASE)

    def test_network_passphrase_mismatch_raise(self):
        uri = "web+kuknos:tx?xdr=AAAAAP%2Byw%2BZEuNg533pUmwlYxfrq6%2FBoMJqiJ8vuQhf6rHWmAAAAZAB8NHAAAAABAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABSFVHAAAAAABAH0wIyY3BJBS2qHdRPAV80M8hF7NBpxRjXyjuT9kEbH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAAAAAAAAAA%3D&callback=url%3Ahttps%3A%2F%2FsomeSigningService.com&replace=sourceAccount%3AX%3BX%3Aaccount%20on%20which%20to%20create%20the%20trustline&pubkey=GAU2ZSYYEYO5S5ZQSMMUENJ2TANY4FPXYGGIMU6GMGKTNVDG5QYFW6JS&msg=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=8uiZ2r7KT3gRsO%2BrzmofGHyl%2FLFMfOgNtx5oOddK2rAy8M%2BOgBYOSQpASNbIm%2BIvZVojxv8tKTYuzOkbyhPODA%3D%3D"
        with pytest.raises(
            ValueError,
            match="The `network_passphrase` in the function parameter does not "
            "match the `network_passphrase` in the uri.",
        ):
            TransactionKuknosUri.from_uri(uri, Network.PUBLIC_NETWORK_PASSPHRASE)


class TestPayKuknosUri:
    @pytest.mark.parametrize(
        "destination, amount, asset, memo, callback, message, network_passphrase, origin_domain, signature, signer, uri",
        [
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                None,
                TextMemo("skdjfasf"),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC",
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=skdjfasf&memo_type=MEMO_TEXT&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=tbsLtlK%2FfouvRWk2UWFP47yHYeI1g1NEC%2FfEQvuXG6V8P%2BbeLxplYbOVtTk1g94Wp97cHZ3pVJy%2FtZNYobl3Cw%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                None,
                TextMemo("skdjfasf"),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                "testSignature",
                "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC",
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=skdjfasf&memo_type=MEMO_TEXT&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=tbsLtlK%2FfouvRWk2UWFP47yHYeI1g1NEC%2FfEQvuXG6V8P%2BbeLxplYbOVtTk1g94Wp97cHZ3pVJy%2FtZNYobl3Cw%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                None,
                TextMemo("skdjfasf"),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                None,
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=skdjfasf&memo_type=MEMO_TEXT&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                None,
                TextMemo("skdjfasf"),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                "testSignature",
                None,
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=skdjfasf&memo_type=MEMO_TEXT&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=testSignature",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                None,
                TextMemo("skdjfasf"),
                None,
                "_" * 300,
                None,
                "someDomain.com",
                None,
                "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC",
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=skdjfasf&memo_type=MEMO_TEXT&msg=____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________&origin_domain=someDomain.com&signature=d94yTtEX0PMUDwwYfzLuVx6luuEiVlxyVQrkR%2FM4NIundX2VqXLVE%2F6FX8G5x4MZ1qc0u661t4Rfu5SKyTIjCg%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                None,
                NoneMemo(),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=t9glBiurQ1MUyk3T5BIqxgJwbrNT1ZDIzQ6aKDJmPgM8heN1NEk%2FusfMq6lSaqtxUuysfZisgPM8TiSY0ckyCw%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                None,
                TextMemo("skdjfasf"),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=skdjfasf&memo_type=MEMO_TEXT&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=tbsLtlK%2FfouvRWk2UWFP47yHYeI1g1NEC%2FfEQvuXG6V8P%2BbeLxplYbOVtTk1g94Wp97cHZ3pVJy%2FtZNYobl3Cw%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                Asset.native(),
                TextMemo("skdjfasf"),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=skdjfasf&memo_type=MEMO_TEXT&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=tbsLtlK%2FfouvRWk2UWFP47yHYeI1g1NEC%2FfEQvuXG6V8P%2BbeLxplYbOVtTk1g94Wp97cHZ3pVJy%2FtZNYobl3Cw%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                Asset.native(),
                IdMemo(10086),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=10086&memo_type=MEMO_ID&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=cTyphv1qE6YqnwKu1O4psEzA8O6vNYu%2FDbvGb0Nu53V%2FL8U7LoGknX1JOGLsgGjOXdfAmJbG8rxF8I9DD%2BvjCA%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                Asset.native(),
                HashMemo(
                    "218a3ef357324c496d07f7d7b31be5c2a11a1ac44af9b81938a6c5b9c0684af4"
                ),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=IYo%2B81cyTEltB%2FfXsxvlwqEaGsRK%2BbgZOKbFucBoSvQ%3D&memo_type=MEMO_HASH&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=CzqyewhypDQGCBlvxSj%2BazIm5iS2GDqcOlBeXT%2FB7s8ogEXC8hNa6HjOArdbTkvNCUvTl6lgyKOj%2FeeNE%2BA5DQ%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                Asset.native(),
                ReturnHashMemo(
                    "218a3ef357324c496d07f7d7b31be5c2a11a1ac44af9b81938a6c5b9c0684af4"
                ),
                None,
                "pay me with paymons",
                None,
                "someDomain.com",
                None,
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&memo=IYo%2B81cyTEltB%2FfXsxvlwqEaGsRK%2BbgZOKbFucBoSvQ%3D&memo_type=MEMO_RETURN&msg=pay%20me%20with%20paymons&origin_domain=someDomain.com&signature=4OJcgA0qxjUhqJL79MeK%2BkHgNjdKXiGhufvw2yjcXud7Ce%2BG53N0qSUpgXDT8OBDQRrI7Pe%2FUPu0%2FCM7DJkXAQ%3D%3D",
            ),
            (
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                "120.1234567",
                Asset(
                    "Hello", "GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF"
                ),
                TextMemo("Hello World"),
                "https://example.com/callback",
                "pay me with paymons",
                Network.TESTNET_NETWORK_PASSPHRASE,
                "someDomain.com",
                "testSignature",
                Keypair.from_secret(
                    "SBPOVRVKTTV7W3IOX2FJPSMPCJ5L2WU2YKTP3HCLYPXNI5MDIGREVNYC"
                ),
                "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&asset_code=Hello&asset_issuer=GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF&memo=Hello%20World&memo_type=MEMO_TEXT&callback=url%3Ahttps%3A%2F%2Fexample.com%2Fcallback&msg=pay%20me%20with%20paymons&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=k5cDMVTD2W2lKeEGqakjOTf3aPuPumlr8ObBOvauaa2QiXqa7%2Bw9WRgtmo6NaPXdOoFG5ScUIp9k7PdeuPieCw%3D%3D",
            ),
        ],
    )
    def test_to_uri(
        self,
        destination,
        amount,
        asset,
        memo,
        callback,
        message,
        network_passphrase,
        origin_domain,
        signature,
        signer,
        uri,
    ):
        uri_builder = PayKuknosUri(
            destination=destination,
            amount=amount,
            asset=asset,
            memo=memo,
            callback=callback,
            message=message,
            network_passphrase=network_passphrase,
            origin_domain=origin_domain,
            signature=signature,
        )
        if signer:
            uri_builder.sign(signer)
        assert uri_builder.to_uri() == uri
        assert PayKuknosUri.from_uri(uri_builder.to_uri()).to_uri() == uri

    def test_message_too_long_raise(self):
        message = "_" * 301
        with pytest.raises(ValueError, match="Message must not exceed 300 characters."):
            PayKuknosUri(
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO",
                message=message,
            )

    def test_invalid_memo_raise(self):
        memo = "invalid memo"
        with pytest.raises(ValueError, match="Invalid memo."):
            PayKuknosUri(
                "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO", memo=memo
            )

    def test_equal(self):
        assert PayKuknosUri(
            "GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO"
        ) == PayKuknosUri("GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO")

    def test_invalid_callback_raise(self):
        uri = "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&asset_code=Hello&asset_issuer=GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF&memo=Hello%20World&memo_type=MEMO_TEXT&callback=https%3A%2F%2Fexample.com%2Fcallback&msg=pay%20me%20with%20paymons&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=k5cDMVTD2W2lKeEGqakjOTf3aPuPumlr8ObBOvauaa2QiXqa7%2Bw9WRgtmo6NaPXdOoFG5ScUIp9k7PdeuPieCw%3D%3D"
        with pytest.raises(ValueError, match="`callback` should start with `url:`."):
            PayKuknosUri.from_uri(uri)

    def test_invalid_scheme_raise(self):
        uri = "invalid+web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&asset_code=Hello&asset_issuer=GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF&memo=Hello%20World&memo_type=MEMO_TEXT&callback=url%3Ahttps%3A%2F%2Fexample.com%2Fcallback&msg=pay%20me%20with%20paymons&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=k5cDMVTD2W2lKeEGqakjOTf3aPuPumlr8ObBOvauaa2QiXqa7%2Bw9WRgtmo6NaPXdOoFG5ScUIp9k7PdeuPieCw%3D%3D"
        # TODO: recheck: Kuknos URI scheme should be `web+kuknos`, but got `invalid+web+kuknos`.
        with pytest.raises(ValueError, match="Kuknos URI scheme should be"):
            PayKuknosUri.from_uri(uri)

    def test_invalid_path_raise(self):
        uri = "web+kuknos:invalid_pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&asset_code=Hello&asset_issuer=GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF&memo=Hello%20World&memo_type=MEMO_TEXT&callback=url%3Ahttps%3A%2F%2Fexample.com%2Fcallback&msg=pay%20me%20with%20paymons&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=k5cDMVTD2W2lKeEGqakjOTf3aPuPumlr8ObBOvauaa2QiXqa7%2Bw9WRgtmo6NaPXdOoFG5ScUIp9k7PdeuPieCw%3D%3D"
        with pytest.raises(
            ValueError, match="Kuknos URI path should be `pay`, but got `invalid_pay`."
        ):
            PayKuknosUri.from_uri(uri)

    def test_destination_missing_raise(self):
        uri = "web+kuknos:pay?amount=120.1234567&asset_code=Hello&asset_issuer=GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF&memo=Hello%20World&memo_type=MEMO_TEXT&callback=url%3Ahttps%3A%2F%2Fexample.com%2Fcallback&msg=pay%20me%20with%20paymons&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=k5cDMVTD2W2lKeEGqakjOTf3aPuPumlr8ObBOvauaa2QiXqa7%2Bw9WRgtmo6NaPXdOoFG5ScUIp9k7PdeuPieCw%3D%3D"
        with pytest.raises(ValueError, match="`destination` is missing from uri."):
            PayKuknosUri.from_uri(uri)

    def test_memo_no_value_raise(self):
        uri = "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&asset_code=Hello&asset_issuer=GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF&memo_type=MEMO_TEXT&callback=url%3Ahttps%3A%2F%2Fexample.com%2Fcallback&msg=pay%20me%20with%20paymons&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=k5cDMVTD2W2lKeEGqakjOTf3aPuPumlr8ObBOvauaa2QiXqa7%2Bw9WRgtmo6NaPXdOoFG5ScUIp9k7PdeuPieCw%3D%3D"
        with pytest.raises(ValueError, match="`memo` is missing from uri."):
            PayKuknosUri.from_uri(uri)

    def test_invalid_memo_type_raise(self):
        uri = "web+kuknos:pay?destination=GCALNQQBXAPZ2WIRSDDBMSTAKCUH5SG6U76YBFLQLIXJTF7FE5AX7AOO&amount=120.1234567&asset_code=Hello&asset_issuer=GBDIT5GUJ7R5BXO3GJHFXJ6AZ5UQK6MNOIDMPQUSMXLIHTUNR2Q5CFNF&memo=Hello%20World&memo_type=MEMO_TEXT_INVALID&callback=url%3Ahttps%3A%2F%2Fexample.com%2Fcallback&msg=pay%20me%20with%20paymons&network_passphrase=Test%20SDF%20Network%20%3B%20September%202015&origin_domain=someDomain.com&signature=k5cDMVTD2W2lKeEGqakjOTf3aPuPumlr8ObBOvauaa2QiXqa7%2Bw9WRgtmo6NaPXdOoFG5ScUIp9k7PdeuPieCw%3D%3D"
        with pytest.raises(ValueError, match="Invalid `memo_type`."):
            PayKuknosUri.from_uri(uri)


class TestReplacement:
    def test_equal(self):
        assert Replacement(
            "sourceAccount", "X", "account on which to create the trustline"
        ) == Replacement(
            "sourceAccount", "X", "account on which to create the trustline"
        )
