import abc
import typing

type ArgType = typing.Any


class CheckerType(typing.Protocol):
    @abc.abstractmethod
    def __call__(self, __arg: ArgType, /) -> None:
        raise NotImplementedError

