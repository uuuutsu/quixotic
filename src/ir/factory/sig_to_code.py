from __future__ import annotations

import functools
import typing

import attrs

from src.common import tools
from src.ir import opcodes

P = typing.ParamSpec("P")
R = typing.TypeVar("R")


def signature_to_opcode(func: typing.Callable[P, None]) -> typing.Callable[P, opcodes.Opcode]:
    annot = typing.get_type_hints(func)
    annot.pop("return", None)

    cls = type(
        func.__name__,
        (opcodes.Opcode,),
        {
            "__annotations__": annot,
            "__attrs__": func.__code__.co_varnames,
        },
    )
    opcode_cls = attrs.frozen(cls)
    echo = tools.signature_to_echo(func)

    @functools.wraps(func)
    def _inner(*args: P.args, **kwargs: P.kwargs) -> opcodes.Opcode:
        func(*args, **kwargs)
        return typing.cast(opcodes.Opcode, opcode_cls(**echo(*args, **kwargs)))

    return _inner
