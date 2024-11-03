import abc
import typing


class BuilderType[T](typing.Protocol):
    @abc.abstractmethod
    def build(self) -> T:
        raise NotImplementedError
