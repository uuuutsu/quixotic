from __future__ import annotations

import functools
import types
import typing

from src.common import tools

from . import exceptions, utils

P = typing.ParamSpec("P")
R = typing.TypeVar("R")

type KwargsType = dict[str, typing.Any]
type PerfectCheckType = typing.Callable[[KwargsType], bool]
type CheckType = str | types.CodeType | PerfectCheckType


def check_arg(check: CheckType) -> utils.BaseChain[typing.Callable[P, R], typing.Callable[P, R]]:
    check_func = check_to_callable(check)

    @utils.BaseChain
    def _checked_function_factory(func: typing.Callable[P, R]) -> typing.Callable[P, R]:
        echo = tools.signature_to_echo(func)

        @functools.wraps(func)
        def _checked(*args: P.args, **kwargs: P.kwargs) -> R:
            if not check_func(echo(*args, **kwargs)):
                exceptions.CheckArgError(func, check, args, kwargs)
            return func(*args, **kwargs)

        return _checked

    return _checked_function_factory


def check_to_callable(check: CheckType) -> PerfectCheckType:
    match check:
        case str():
            exc = compile(check, "<check>", "eval")
            return typing.cast(PerfectCheckType, functools.partial(eval, exc))
        case types.CodeType():
            return typing.cast(PerfectCheckType, functools.partial(eval, check))
        case _:
            return check
