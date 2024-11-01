from __future__ import annotations

import functools
import inspect
import typing

import attrs

from . import base

P = typing.ParamSpec("P")


def opcode_from_sig(func: typing.Callable[P, None]) -> typing.Callable[P, base.Opcode]:
    annot = typing.get_type_hints(func)
    annot.pop("return", None)

    cls = type(
        func.__name__,
        (base.Opcode,),
        {
            "__attrs__": func.__code__.co_varnames,
            "__annotations__": annot,
        },
    )
    for key, value in inspect.signature(func).parameters.items():
        if value.default is not inspect.Parameter.empty:
            setattr(cls, key, value.default)

    opcode_cls = attrs.frozen(cls)

    @functools.wraps(func)
    def opcode(*args: P.args, **kwargs: P.kwargs) -> base.Opcode:
        return typing.cast(base.Opcode, opcode_cls(*args, **kwargs))

    return opcode
