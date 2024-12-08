import typing

from src import ir
from src.ir import types

from .dtypes import Array, Const, Unit

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


@ir.signature_to_opcode
def procedure(opcodes: typing.Sequence[types.OpcodeType]) -> None: ...


@ir.signature_to_opcode
def add(left: Unit | Int, right: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def move(left: Unit, target: tuple[tuple[Unit, int], ...]) -> None: ...


@ir.signature_to_opcode
def alloc(target: Unit | Array) -> None: ...


@ir.signature_to_opcode
def free(target: Unit | Array) -> None: ...
