from kuknos_sdk import Asset
from kuknos_sdk.call_builder import OrderbookCallBuilder
from tests.call_builder import horizon_url, client


class TestOrderbookCallBuilder:
    def test_init(self):
        selling = Asset(
            "BTC", "GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH"
        )
        buying = Asset.native()
        builder = OrderbookCallBuilder(horizon_url, client, selling, buying)
        assert builder.endpoint == "order_book"
        assert builder.params == {
            "selling_asset_type": selling.type,
            "selling_asset_code": selling.code,
            "selling_asset_issuer": selling.issuer,
            "buying_asset_type": buying.type,
        }
