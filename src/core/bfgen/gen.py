import collections.abc

import attrs

from src import ir
from src.core import prelude
from src.ir import types as ir_types

from . import code, pointer, types, utils


@attrs.frozen
class Generator(prelude.Visitor[None]):
    mapping: collections.abc.Mapping[prelude.OwnerType, int]
    pointer: types.PointerType
    code: types.CodeType[str]

    def decrement(self, owner: prelude.OwnerType) -> None:
        self.pointer.move(self._get_position(owner))
        self.code.write("-")

    def increment(self, owner: prelude.OwnerType) -> None:
        self.pointer.move(self._get_position(owner))
        self.code.write("+")

    def output(self, owner: prelude.OwnerType) -> None:
        self.pointer.move(self._get_position(owner))
        self.code.write(".")

    def input(self, owner: prelude.OwnerType) -> None:
        self.pointer.move(self._get_position(owner))
        self.code.write(",")

    def loop(self, owner: prelude.OwnerType, opcode: ir_types.OpcodeType) -> None:
        self.pointer.move(self._get_position(owner))
        self.code.write("[")

        self.generate(opcode)

        self.pointer.move(self._get_position(owner))
        self.code.write("]")

    def clear(self, owner: prelude.OwnerType) -> None:
        self.pointer.move(self._get_position(owner))
        self.code.write("[-]")

    def comment(self, value: str) -> None:
        utils.check_injection_safety(value)
        self.code.write(value)

    def _get_position(self, owner: prelude.OwnerType) -> int:
        if owner is prelude.CURRENT_OWNER:
            return self.pointer.position
        return self.mapping[owner]

    def generate(self, opcode: ir_types.OpcodeType) -> None:
        self.visit(opcode)


def make_generator(mapping: ir.State[prelude.OwnerType, int]) -> Generator:
    code_ = code.Code()
    return Generator(
        mapping,
        pointer.Pointer(code_),
        code_,
    )
