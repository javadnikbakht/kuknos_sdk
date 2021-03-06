from .operation import Operation
from .. import xdr as kuknos_xdr


class Inflation(Operation):
    """The :class:`Inflation` object, which represents a
    Inflation operation on Kuknos's network.

    This operation runs inflation.

    Threshold: Low

    :param str source: The source account (defaults to transaction source).

    """

    _XDR_OPERATION_TYPE: kuknos_xdr.OperationType = kuknos_xdr.OperationType.INFLATION

    def __init__(self, source: str = None) -> None:
        super().__init__(source)

    def _to_operation_body(self) -> kuknos_xdr.OperationBody:
        body = kuknos_xdr.OperationBody(type=self._XDR_OPERATION_TYPE)
        return body

    @classmethod
    def from_xdr_object(cls, xdr_object: kuknos_xdr.Operation) -> "Inflation":
        """Creates a :class:`Inflation` object from an XDR Operation
        object.

        """
        source = Operation.get_source_from_xdr_obj(xdr_object)
        op = cls(source)
        op._source_muxed = Operation.get_source_muxed_from_xdr_obj(xdr_object)
        return op

    def __str__(self):
        return f"<Inflation [source={self.source}]>"
