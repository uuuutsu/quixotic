import typing

from src import ir

from .dtypes import Array, Const, Unit

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


@ir.signature_to_opcode
def add(augend: Unit | Int, addend: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def and_(left: Unit | Int, right: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def arrload(array: Array, target: UnitSeq, index: UnitSeq | Int) -> None: ...


@ir.signature_to_opcode
def arrstore(array: Array, value: UnitSeq | Int, index: UnitSeq | Int) -> None: ...


@ir.signature_to_opcode
def assign(left: Unit | Int, target: Unit) -> None: ...


@typing.overload
@ir.signature_to_opcode
def callz(value: Unit, if_zero: ir.ProcedureType, else_: None) -> None: ...
@typing.overload
@ir.signature_to_opcode
def callz(value: Unit, if_zero: None, else_: ir.ProcedureType) -> None: ...
@ir.signature_to_opcode
def callz(value: Unit, if_zero: ir.ProcedureType | None, else_: ir.ProcedureType | None) -> None: ...


@ir.signature_to_opcode
def copy(from_: Unit, to_: Unit) -> None: ...


@typing.overload
@ir.signature_to_opcode
def div(left: Unit | Int, right: Unit | Int, quotient: Unit, remainder: None) -> None: ...
@typing.overload
@ir.signature_to_opcode
def div(left: Unit | Int, right: Unit | Int, quotient: None, remainder: Unit) -> None: ...
@typing.overload
@ir.signature_to_opcode
def div(left: Unit | Int, right: Unit | Int, quotient: Unit, remainder: Unit) -> None: ...
@ir.signature_to_opcode
def div(left: Unit | Int, right: Unit | Int, quotient: Unit | None, remainder: Unit | None) -> None: ...


@ir.signature_to_opcode
def move(from_: Unit, to_: tuple[tuple[Unit, int], ...]) -> None: ...


@ir.signature_to_opcode
def mul(left: Unit | Int, right: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def not_(left: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def or_(left: Unit | Int, right: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def sub(left: Unit | Int, right: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def xor(left: Unit | Int, right: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def clear(left: Unit) -> None: ...


@ir.signature_to_opcode
def alloc(left: Unit | Array) -> None: ...


@ir.signature_to_opcode
def free(left: Unit | Array) -> None: ...
