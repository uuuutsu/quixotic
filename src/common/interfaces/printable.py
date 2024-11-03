import abc
import typing


class PrintableType(typing.Protocol):
    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
