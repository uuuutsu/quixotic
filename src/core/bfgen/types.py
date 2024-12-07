import abc
import typing


class CodeType[T: str](typing.Protocol):
    @abc.abstractmethod
    def write(self, __data: T) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def read(self) -> T:
        raise NotImplementedError


class PointerType(typing.Protocol):
    position: int

    @abc.abstractmethod
    def move(self, __pos: int) -> None:
        raise NotImplementedError
