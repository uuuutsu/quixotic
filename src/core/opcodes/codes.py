from src import ir

from .owner import CURRENT_OWNER, OwnerType


@ir.signature_to_opcode
def decrement(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def increment(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def output(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def input(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def loop(owner: OwnerType, proc: ir.ProcedureType) -> None: ...


@ir.signature_to_opcode
def clear(owner: OwnerType) -> None: ...


@ir.signature_to_opcode
def compiler_injection(value: str, end_owner: OwnerType = CURRENT_OWNER) -> None: ...


@ir.signature_to_opcode
def comment_injection(value: str, owner: OwnerType = CURRENT_OWNER, end_owner: OwnerType = CURRENT_OWNER) -> None:
    ...
    # value = utils.check_injection_safety_attrs(value)


@ir.signature_to_opcode
def code_injection(value: str = "", end_owner: OwnerType = CURRENT_OWNER) -> None: ...
