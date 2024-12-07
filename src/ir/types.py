import abc
import collections.abc
import typing


class OpcodeType(typing.Protocol):
    identity: typing.ClassVar[str]

    @abc.abstractmethod
    def get_attrs(self) -> dict[str, typing.Any]:
        raise NotImplementedError


class VisitorType[I, O](typing.Protocol):
    @abc.abstractmethod
    def visit(self, __expr: I) -> O:
        raise NotImplementedError


class DType(typing.Protocol):
    @abc.abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError


class StateType[K: DType, V: typing.Any](collections.abc.MutableMapping[K, V]): ...
