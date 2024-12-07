import abc
import typing

from src import ir
from src.ir import types

from .dtypes import Array, Const, Unit

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


class Visitor[T](ir.Visitor[T]):
    @abc.abstractmethod
    def procedure(self, opcodes: typing.Sequence[types.OpcodeType]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, left: Unit | Int, right: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def move(self, left: Unit, target: tuple[tuple[Unit, int], ...]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def alloc(self, target: Unit | Array) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def free(self, target: Unit | Array) -> None:
        raise NotImplementedError
