from __future__ import annotations

import functools
import typing

import attrs

from src.common import tools
from src.ir import opcode

from . import utils

P = typing.ParamSpec("P")
R = typing.TypeVar("R")


@utils.BaseChain
def signature_to_opcode(func: typing.Callable[P, None]) -> typing.Callable[P, opcode.BaseOpcode]:
    annot = typing.get_type_hints(func)
    annot.pop("return", None)

    cls = type(
        func.__name__,
        (opcode.BaseOpcode,),
        {
            "__annotations__": annot,
            "__attrs__": func.__code__.co_varnames,
        },
    )
    opcode_cls = attrs.frozen(cls)
    echo = tools.signature_to_echo(func)

    @functools.wraps(func)
    def _inner(*args: P.args, **kwargs: P.kwargs) -> opcode.BaseOpcode:
        return typing.cast(opcode.BaseOpcode, opcode_cls(**echo(*args, **kwargs)))

    return _inner
