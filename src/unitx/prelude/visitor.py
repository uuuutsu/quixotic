import abc

from src import ir

from .dtypes import Array, Const, Unit

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


class Visitor[T](ir.Visitor[T]):
    @abc.abstractmethod
    def add(self, augend: Unit | Int, addend: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def move(self, from_: Unit, to_: tuple[tuple[Unit, int], ...]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def alloc(self, target: Unit | Array) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def free(self, target: Unit | Array) -> None:
        raise NotImplementedError
