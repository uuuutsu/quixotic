import abc

from src import ir

from .dtypes import Array, Const, Unit

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


class Walker(ir.WalkerBase):
    @abc.abstractmethod
    def add(self, augend: Unit | Int, addend: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def and_(self, left: Unit | Int, right: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def arrload(self, array: Array, target: UnitSeq, index: UnitSeq | Int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def arrstore(self, array: Array, value: UnitSeq | Int, index: UnitSeq | Int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def assign(self, value: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def callz(self, value: Unit, if_zero: ir.ProcedureType | None, else_: ir.ProcedureType | None) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def copy(self, from_: Unit, to_: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def div(self, dividend: Unit | Int, divisor: Unit | Int, quotient: Unit | None, remainder: Unit | None) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def move(self, from_: Unit, to_: tuple[tuple[Unit, int], ...]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def mul(self, multiplicand: Unit | Int, multiplier: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def not_(self, operand: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def or_(self, left: Unit, right: Unit, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def sub(self, minuend: Unit | Int, subtrahend: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def xor(self, left: Unit, right: Unit, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def alloc(self, target: Unit | Array) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def free(self, target: Unit | Array) -> None:
        raise NotImplementedError
