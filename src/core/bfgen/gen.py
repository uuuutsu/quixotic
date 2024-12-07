import attrs

from src import ir
from src.core import prelude
from src.ir import types as ir_types

from . import code, pointer, types


@attrs.frozen
class Generator(prelude.Visitor[None]):
    mapping: ir.State[prelude.OwnerType, int]
    pointer: types.PointerType
    code: types.CodeType[str]

    def decrement(self, owner: prelude.OwnerType) -> None:
        raise NotImplementedError

    def increment(self, owner: prelude.OwnerType) -> None:
        raise NotImplementedError

    def output(self, owner: prelude.OwnerType) -> None:
        raise NotImplementedError

    def input(self, owner: prelude.OwnerType) -> None:
        raise NotImplementedError

    def loop(self, owner: prelude.OwnerType, opcode: ir_types.OpcodeType) -> None:
        raise NotImplementedError

    def clear(self, owner: prelude.OwnerType) -> None:
        raise NotImplementedError

    def comment(self, value: str) -> None: ...

    def generate(self, opcode: ir_types.OpcodeType) -> None:
        self.visit(opcode)


def make_generator(mapping: ir.State[prelude.OwnerType, int]) -> Generator:
    code_ = code.Code()
    return Generator(
        mapping,
        pointer.Pointer(code_),
        code_,
    )
