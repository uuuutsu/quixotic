import abc
import typing

from src.widex.common import dtypes


@typing.runtime_checkable
class OpcodeType(typing.Protocol):
    identity: str

    @abc.abstractmethod
    def get_attrs(self) -> dict[str, dtypes.DType]:
        raise NotImplementedError
