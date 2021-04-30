import pytest

from kuknos_sdk import Asset
from kuknos_sdk.call_builder import TradeAggregationsCallBuilder
from tests.call_builder import horizon_url, client
from kuknos_sdk.exceptions import ValueError


class TestTradeAggregationsCallBuilder:
    def test_init(self):
        base = Asset("XCN", "GCOMOKXUA4TAEBB2QDHZD53SNRWKNTJMVEFLE47JYN5HS7KNLOABVA4Z")
        counter = Asset.native()
        resolution = 300000
        builder = TradeAggregationsCallBuilder(
            horizon_url, client, base=base, counter=counter, resolution=resolution
        )
        assert builder.endpoint == "trade_aggregations"
        assert builder.params == {
            "base_asset_type": base.type,
            "base_asset_code": base.code,
            "base_asset_issuer": base.issuer,
            "counter_asset_type": counter.type,
            "resolution": str(resolution),
        }

    def test_invalid_resolution_raise(self):
        base = Asset("XCN", "GCOMOKXUA4TAEBB2QDHZD53SNRWKNTJMVEFLE47JYN5HS7KNLOABVA4Z")
        counter = Asset.native()
        resolution = 1000
        with pytest.raises(
            ValueError, match="Invalid resolution: {}".format(resolution)
        ):
            TradeAggregationsCallBuilder(
                horizon_url, client, base=base, counter=counter, resolution=resolution
            )

    def test_invalid_offset_raise(self):
        base = Asset("XCN", "GCOMOKXUA4TAEBB2QDHZD53SNRWKNTJMVEFLE47JYN5HS7KNLOABVA4Z")
        counter = Asset.native()
        resolution = 300000
        offset = 600000
        with pytest.raises(ValueError, match="Invalid offset: {}".format(offset)):
            TradeAggregationsCallBuilder(
                horizon_url,
                client,
                base=base,
                counter=counter,
                resolution=resolution,
                offset=offset,
            )
