from __future__ import annotations

import functools
import inspect
import typing

import attrs

from . import opcode

P = typing.ParamSpec("P")


def opcode_factory(func: typing.Callable[P, None]) -> typing.Callable[P, opcode.BaseOpcode]:
    annot = typing.get_type_hints(func)
    annot.pop("return", None)

    cls = type(
        func.__name__,
        (opcode.BaseOpcode,),
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
    def _inner(*args: P.args, **kwargs: P.kwargs) -> opcode.BaseOpcode:
        return typing.cast(opcode.BaseOpcode, opcode_cls(*args, **kwargs))

    return _inner
