from src import ir

from .dtypes import Array, Const, Unit

type Int = Const[int]
type UnitSeq = Const[tuple[Unit, ...]]


@ir.signature_to_opcode
def add(left: Unit | Int, right: Unit | Int, target: Unit) -> None: ...


@ir.signature_to_opcode
def move(left: Unit, target: tuple[tuple[Unit, int], ...]) -> None: ...


@ir.signature_to_opcode
def alloc(left: Unit | Array) -> None: ...


@ir.signature_to_opcode
def free(left: Unit | Array) -> None: ...
