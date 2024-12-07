from src import ir
from src.ir import types

from .dtypes import OwnerType


@ir.signature_to_opcode
def decrement(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def increment(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def output(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def input(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def loop(owner: OwnerType, code: types.OpcodeType) -> None: ...


@ir.signature_to_opcode
def clear(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def comment(value: str) -> None: ...
