from __future__ import annotations

import functools
import typing

import attrs

from src.common import tools

from . import base

P = typing.ParamSpec("P")
R = typing.TypeVar("R")


@tools.BaseChain
def signature_to_opcode(func: typing.Callable[P, None]) -> typing.Callable[P, dict[str, typing.Any]]:
    annot = typing.get_type_hints(func)
    annot.pop("return", None)

    cls = type(
        func.__name__,
        (base.BaseOpcode,),
        {
            "__annotations__": annot,
            "__attrs__": func.__code__.co_varnames,
        },
    )
    opcode_cls = attrs.frozen(cls)
    echo = tools.signature_to_echo(func)

    @functools.wraps(func)
    def _inner(*args: P.args, **kwargs: P.kwargs) -> base.BaseOpcode:
        return typing.cast(base.BaseOpcode, opcode_cls(**echo(*args, **kwargs)))

    return _inner
