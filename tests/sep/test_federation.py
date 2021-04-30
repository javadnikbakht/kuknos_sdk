import pytest

from kuknos_sdk.client.aiohttp_client import AiohttpClient
from kuknos_sdk.sep.exceptions import (
    InvalidFederationAddress,
    FederationServerNotFoundError,
    BadFederationResponseError,
)
from kuknos_sdk.sep.federation import (
    resolve_kuknos_address,
    resolve_account_id,
    FederationRecord,
    split_kuknos_address,
)
from kuknos_sdk.exceptions import ValueError


class TestFederation:
    ACCOUNT_ID = "GAWCQ74PIJO2NH6F3KZ4AMX27UAKBXWC7KG3FLYJOFIMRQF3RSZHCOVN"
    STELLAR_ADDRESS = "hello*overcat.me"
    DOMAIN = "overcat.me"
    FEDERATION_SERVER = "https://federation.overcat.workers.dev/"
    FEDERATION_RECORD = FederationRecord(
        kuknos_address=STELLAR_ADDRESS,
        account_id=ACCOUNT_ID,
        memo_type="text",
        memo="Nice to meet you :-)",
    )

    def test_resolve_by_kuknos_address_sync(self):
        record = resolve_kuknos_address(self.STELLAR_ADDRESS)
        assert record == self.FEDERATION_RECORD

    @pytest.mark.asyncio
    async def test_resolve_by_kuknos_address_async(self):
        record = await resolve_kuknos_address(
            self.STELLAR_ADDRESS, client=AiohttpClient()
        )
        assert record == self.FEDERATION_RECORD

    def test_resolve_by_kuknos_address_federation_not_found_sync(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            resolve_kuknos_address("hello*sdk-test.overcat.me")

    @pytest.mark.asyncio
    async def test_resolve_by_kuknos_address_federation_not_found_async(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            await resolve_kuknos_address(
                "hello*sdk-test.overcat.me", client=AiohttpClient()
            )

    def test_resolve_by_kuknos_address_with_federation_url_sync(self):
        record = resolve_kuknos_address(
            "hello*example.com", federation_url=self.FEDERATION_SERVER
        )
        assert (
            record.account_id
            == "GAWCQ74PIJO2NH6F3KZ4AMX27UAKBXWC7KG3FLYJOFIMRQF3REXAMPLE"
        )

    @pytest.mark.asyncio
    async def test_resolve_by_kuknos_address_with_federation_url_async(self):
        record = await resolve_kuknos_address(
            "hello*example.com",
            federation_url=self.FEDERATION_SERVER,
            client=AiohttpClient(),
        )
        assert (
            record.account_id
            == "GAWCQ74PIJO2NH6F3KZ4AMX27UAKBXWC7KG3FLYJOFIMRQF3REXAMPLE"
        )

    def test_resolve_by_account_id_with_domain_sync(self):
        record = resolve_account_id(self.ACCOUNT_ID, domain=self.DOMAIN)
        assert record == self.FEDERATION_RECORD

    @pytest.mark.asyncio
    async def test_resolve_by_account_id_with_domain_async(self):
        record = await resolve_account_id(
            self.ACCOUNT_ID, domain=self.DOMAIN, client=AiohttpClient()
        )
        assert record == self.FEDERATION_RECORD

    def test_resolve_by_account_id_without_domain_and_federation_url(self):
        with pytest.raises(
            ValueError, match="You should provide either `domain` or `federation_url`."
        ):
            resolve_account_id(self.ACCOUNT_ID)

    def test_resolve_by_account_id_federation_not_found_sync(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            resolve_account_id(self.ACCOUNT_ID, domain="sdk-test.overcat.me")

    @pytest.mark.asyncio
    async def test_resolve_by_account_id_federation_not_found_async(self):
        with pytest.raises(
            FederationServerNotFoundError,
            match="Unable to find federation server at sdk-test.overcat.me.",
        ):
            await resolve_account_id(
                self.ACCOUNT_ID, domain="sdk-test.overcat.me", client=AiohttpClient()
            )

    def test_not_found_record_at_federation(self):
        with pytest.raises(BadFederationResponseError) as err:
            resolve_kuknos_address("not_found*overcat.me")
        assert err.value.status == 404

    def test_split_address(self):
        assert split_kuknos_address(self.STELLAR_ADDRESS) == {
            "name": "hello",
            "domain": "overcat.me",
        }

    @pytest.mark.parametrize("kuknos_address", ["", "hey", "hey*hello*overcat.me"])
    def test_split_invalid_address(self, kuknos_address):
        with pytest.raises(InvalidFederationAddress):
            split_kuknos_address(kuknos_address)

    def test_invalid_client(self):
        client = "BAD TYPE"
        with pytest.raises(
            TypeError,
            match="This `client` class should be an instance "
            "of `kuknos_sdk.client.base_async_client.BaseAsyncClient` "
            "or `kuknos_sdk.client.base_sync_client.BaseSyncClient`.",
        ):
            resolve_account_id(self.ACCOUNT_ID, domain=self.DOMAIN, client=client)

        with pytest.raises(
            TypeError,
            match="This `client` class should be an instance "
            "of `kuknos_sdk.client.base_async_client.BaseAsyncClient` "
            "or `kuknos_sdk.client.base_sync_client.BaseSyncClient`.",
        ):
            resolve_kuknos_address(self.STELLAR_ADDRESS, client=client)
