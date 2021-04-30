import pytest

from kuknos_sdk.client.aiohttp_client import AiohttpClient
from kuknos_sdk.sep.exceptions import KuknosTomlNotFoundError
from kuknos_sdk.sep.kuknos_toml import fetch_kuknos_toml


class TestKuknosToml:
    def test_get_success_sync(self):
        toml = fetch_kuknos_toml("overcat.me", None)
        assert toml.get("FEDERATION_SERVER") == "https://federation.overcat.workers.dev"

    @pytest.mark.asyncio
    async def test_get_success_async(self):
        client = AiohttpClient()
        toml = await fetch_kuknos_toml("overcat.me", client)
        assert toml.get("FEDERATION_SERVER") == "https://federation.overcat.workers.dev"

    def test_get_success_http(self):
        toml = fetch_kuknos_toml("overcat.me", None, True)
        assert toml.get("FEDERATION_SERVER") == "https://federation.overcat.workers.dev"

    def test_get_not_found(self):
        with pytest.raises(KuknosTomlNotFoundError):
            fetch_kuknos_toml("httpbin.org")

    def test_invalid_client(self):
        client = "BAD TYPE"
        with pytest.raises(
            TypeError,
            match="This `client` class should be an instance "
            "of `kuknos_sdk.client.base_async_client.BaseAsyncClient` "
            "or `kuknos_sdk.client.base_sync_client.BaseSyncClient`.",
        ):
            fetch_kuknos_toml("httpbin.org", client)
