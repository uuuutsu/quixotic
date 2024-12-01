import typing

import attrs

from src import ir
from src.unitx import opcodes
from src.unitx.opcodes.dtypes import Array, Const, Unit

from .state import State

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


@attrs.frozen
class Emulator(opcodes.Walker):
    state: State = attrs.field(factory=State)

    @abc.abstractmethod
    def add(self, augend: Unit | Int, addend: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def and_(self, left: Unit | Int, right: Unit | Int, target: Unit) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def arrload(self, array: Array, target: UnitSeq, index: UnitSeq | Int) -> None:
        raise NotImplementedError

    def arrstore(self, array: Array, value: UnitSeq | Int, index: UnitSeq | Int) -> None:
        self.state[array][self._get_value(index)] = self._get_value(value)

    def assign(self, left: Unit | Int, target: Unit) -> None:
        self.state[target] = self._get_value(left)

    def callz(self, value: Unit, if_zero: ir.ProcedureType | None, else_: ir.ProcedureType | None) -> None:
        if (self.state[value] != 0) and if_zero:
            self.walk(if_zero)
        elif else_:
            self.walk(else_)

    def copy(self, from_: Unit, to_: Unit) -> None:
        self.state[to_] = self.state[from_]

    def div(self, left: Unit | Int, right: Unit | Int, quotient: Unit | None, remainder: Unit | None) -> None:
        if remainder:
            self.state[remainder] = self._get_value(left) % self._get_value(right)
        if quotient:
            self.state[quotient] = self._get_value(left) // self._get_value(right)

    def move(self, from_: Unit, to_: tuple[tuple[Unit, int], ...]) -> None:
        for unit, scale in to_:
            self.state[unit] = self.state[from_] * scale

        self.clear(from_)

    def mul(self, left: Unit | Int, right: Unit | Int, target: Unit) -> None:
        self.state[target] = self._get_value(left) * self._get_value(right)

    def not_(self, left: Unit | Int, target: Unit) -> None:
        self.state[target] = ~self._get_value(left)

    def or_(self, left: Unit, right: Unit, target: Unit) -> None:
        self.state[target] = self._get_value(left) | self._get_value(right)

    def sub(self, left: Unit | Int, right: Unit | Int, target: Unit) -> None:
        self.state[target] = self._get_value(left) - self._get_value(right)

    def xor(self, left: Unit, right: Unit, target: Unit) -> None:
        self.state[target] = self._get_value(left) ^ self._get_value(right)

    def clear(self, target: Unit) -> None:
        self.state[target] = 0

    def alloc(self, target: Unit | Array) -> None:
        match target:
            case Unit():
                self.state[target] = 0
            case Array():
                self.state[target] = [0] * target.granularity * target.size

    def free(self, target: Unit | Array) -> None:
        del self.state[target]

    @typing.overload
    def _get_value[T](self, obj: Unit | UnitSeq) -> int: ...
    @typing.overload
    def _get_value[T](self, obj: Array) -> list[int]: ...
    @typing.overload
    def _get_value[T](self, obj: Const[T]) -> T: ...
    def _get_value[T](self, obj: Unit | UnitSeq | Array | Const[T]) -> int | list[int] | T:
        match obj:
            case Unit() | Array():
                return self.state[obj]
            case Const():
                if isinstance(obj.value, tuple) and all(isinstance(o, Unit) for o in obj.value):
                    return int.from_bytes(bytes(map(self._get_value, obj.value)), "little", signed=False)
                return obj.value  # type: ignore
