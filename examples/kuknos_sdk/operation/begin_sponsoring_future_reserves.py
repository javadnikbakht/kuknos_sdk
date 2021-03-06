from .operation import Operation
from .utils import check_ed25519_public_key
from .. import xdr as kuknos_xdr
from ..keypair import Keypair
from ..strkey import StrKey


class BeginSponsoringFutureReserves(Operation):
    """The :class:`BeginSponsoringFutureReserves` object, which represents a BeginSponsoringFutureReserves
    operation on Kuknos's network.

    Establishes the is-sponsoring-future-reserves-for relationship between the source account and sponsoredID.
    See `Sponsored Reserves <https://developers.kuknos.org/docs/glossary/sponsored-reserves/>_` for more information.

    See `Begin Sponsoring Future Reserves
    <https://developers.kuknos.org/docs/start/list-of-operations/#begin-sponsoring-future-reserves>_`.

    Threshold: Medium

    :param sponsored_id: The sponsored account id.
    :param source: The source account (defaults to transaction source).
    """

    _XDR_OPERATION_TYPE: kuknos_xdr.OperationType = kuknos_xdr.OperationType.BEGIN_SPONSORING_FUTURE_RESERVES

    def __init__(self, sponsored_id: str, source: str = None) -> None:
        super().__init__(source)
        check_ed25519_public_key(sponsored_id)
        self.sponsored_id: str = sponsored_id

    def _to_operation_body(self) -> kuknos_xdr.OperationBody:
        sponsored_id = Keypair.from_public_key(self.sponsored_id).xdr_account_id()
        begin_sponsoring_future_reserves_op = kuknos_xdr.BeginSponsoringFutureReservesOp(
            sponsored_id=sponsored_id
        )
        body = kuknos_xdr.OperationBody(
            type=self._XDR_OPERATION_TYPE,
            begin_sponsoring_future_reserves_op=begin_sponsoring_future_reserves_op,
        )
        return body

    @classmethod
    def from_xdr_object(
        cls, xdr_object: kuknos_xdr.Operation
    ) -> "BeginSponsoringFutureReserves":
        """Creates a :class:`BeginSponsoringFutureReserves` object from an XDR Operation
        object.
        """
        source = Operation.get_source_from_xdr_obj(xdr_object)
        assert xdr_object.body.begin_sponsoring_future_reserves_op is not None
        assert (
            xdr_object.body.begin_sponsoring_future_reserves_op.sponsored_id.account_id.ed25519
            is not None
        )
        sponsored_id = StrKey.encode_ed25519_public_key(
            xdr_object.body.begin_sponsoring_future_reserves_op.sponsored_id.account_id.ed25519.uint256
        )
        op = cls(source=source, sponsored_id=sponsored_id)
        op._source_muxed = Operation.get_source_muxed_from_xdr_obj(xdr_object)
        return op

    def __str__(self):
        return f"<BeginSponsoringFutureReserves [sponsored_id={self.sponsored_id}, source={self.source}]>"
