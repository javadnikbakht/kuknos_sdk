from .operation import Operation
from .. import xdr as kuknos_xdr


class EndSponsoringFutureReserves(Operation):
    """The :class:`EndSponsoringFutureReserves` object, which represents a EndSponsoringFutureReserves
    operation on Kuknos's network.

    Terminates the current is-sponsoring-future-reserves-for relationship in which the source account is sponsored.
    See `Sponsored Reserves <https://developers.kuknos.org/docs/glossary/sponsored-reserves/>_` for more information.

    See `End Sponsoring Future Reserves
    <https://developers.kuknos.org/docs/start/list-of-operations/#end-sponsoring-future-reserves>_`.

    Threshold: Medium

    :param source: The source account (defaults to transaction source).
    """

    _XDR_OPERATION_TYPE: kuknos_xdr.OperationType = kuknos_xdr.OperationType.END_SPONSORING_FUTURE_RESERVES

    def __init__(self, source: str = None) -> None:
        super().__init__(source)

    def _to_operation_body(self) -> kuknos_xdr.OperationBody:
        body = kuknos_xdr.OperationBody(type=self._XDR_OPERATION_TYPE)
        return body

    @classmethod
    def from_xdr_object(
        cls, xdr_object: kuknos_xdr.Operation
    ) -> "EndSponsoringFutureReserves":
        """Creates a :class:`EndSponsoringFutureReserves` object from an XDR Operation
        object.
        """
        source = Operation.get_source_from_xdr_obj(xdr_object)
        op = cls(source=source)
        op._source_muxed = Operation.get_source_muxed_from_xdr_obj(xdr_object)
        return op

    def __str__(self):
        return f"<EndSponsoringFutureReserves [source={self.source}]>"
