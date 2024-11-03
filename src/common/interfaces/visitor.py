import abc
import typing


class VisitorType[T](typing.Protocol):
    @abc.abstractmethod
    def visit(self, __codes: T) -> None:
        raise NotImplementedError
