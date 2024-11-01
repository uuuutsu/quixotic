import abc
import typing

from src.widex.common import dtypes


@typing.runtime_checkable
class OpcodeType(typing.Protocol):
    identity: typing.Hashable

    @abc.abstractmethod
    def get_attrs(self) -> dict[str, dtypes.DType]:
        raise NotImplementedError


class ProcedureType(typing.Protocol):
    identity: typing.Hashable

    @abc.abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def __getitem__(self, idx: int) -> OpcodeType:
        raise NotImplementedError

    @abc.abstractmethod
    def __iter__(self) -> typing.Iterable[OpcodeType]:
        raise NotImplementedError
