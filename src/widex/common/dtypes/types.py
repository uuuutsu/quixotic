import abc
import typing


class DType(typing.Protocol):
    name: str | None

    @abc.abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError
