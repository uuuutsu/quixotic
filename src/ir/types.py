import abc
import typing


class OpcodeType(typing.Protocol):
    identity: typing.ClassVar[str]

    @abc.abstractmethod
    def get_attrs(self) -> dict[str, typing.Any]:
        raise NotImplementedError


class OpcodeFactoryType(typing.Protocol):
    @abc.abstractmethod
    def __call__(*args: typing.Any, **kwargs: typing.Any) -> typing.Callable[..., OpcodeType]:
        raise NotImplementedError


class ProcedureType(typing.Protocol):
    @abc.abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def __getitem__(self, idx: int) -> OpcodeType:
        raise NotImplementedError

    @abc.abstractmethod
    def __iter__(self) -> typing.Iterator[OpcodeType]:
        raise NotImplementedError

    @abc.abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError


class WalkerType(typing.Protocol):
    @abc.abstractmethod
    def walk(self, __proc: ProcedureType) -> None:
        raise NotImplementedError


class DType(typing.Protocol):
    name: str | None

    @abc.abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError
