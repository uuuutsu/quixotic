import typing

import attrs

from src.ir import types
from src.unitx import prelude
from src.unitx.prelude.dtypes import Array, Const, Unit

from .state import State

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


@attrs.frozen
class Emulator(prelude.Visitor[None]):
    state: State = attrs.field(factory=State)

    def procedure(self, opcodes: typing.Sequence[types.OpcodeType]) -> None:
        for opcode in opcodes:
            self.visit(opcode)

    def add(self, left: Unit | Int, right: Unit | Int, target: Unit) -> None:
        self.state[target] = self._get_value(left) + self._get_value(right)

    def move(self, left: Unit, target: tuple[tuple[Unit, int], ...]) -> None:
        for unit, scale in target:
            self.state[unit] = self.state[left] * scale

        self.state[left] = 0

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

    def emulate(self, opcode: types.OpcodeType) -> None:
        return self.visit(opcode)
