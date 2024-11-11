from __future__ import annotations

import typing

import multimethod

Params = typing.ParamSpec("Params")
Ret = typing.TypeVar("Ret")
ParamsNew = typing.ParamSpec("ParamsNew")
RetNew = typing.TypeVar("RetNew")


def dummy() -> typing.NoReturn:
    raise NotImplementedError("Erm, what the sigma?")


class DynamicOverload(typing.Generic[Params, Ret]):
    __slots__ = ("_dispatcher",)

    def __init__(
        self,
        func: typing.Callable[Params, Ret] | None = None,
        *,
        dp: multimethod.multidispatch[Ret] | None = None,
    ) -> None:
        if dp is None:
            self._dispatcher = multimethod.multidispatch(func or dummy)
            return
        self._dispatcher = dp
        dp.register(func or dummy)

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> Ret:
        return self._dispatcher(*args, **kwargs)

    def __or__(
        self,
        other: typing.Callable[ParamsNew, RetNew] | DynamicOverload[ParamsNew, RetNew],
    ) -> DynamicOverload[Params, Ret] | DynamicOverload[ParamsNew, RetNew]:
        return type(self)(other, dp=self._dispatcher)  # type: ignore


P = typing.ParamSpec("P")
R = typing.TypeVar("R")
DecRetType = typing.TypeVar("DecRetType")


def dp_factory(
    name: str,
    *,
    decs: list[typing.Callable[[typing.Callable[..., typing.Any]], typing.Callable[P, R]]],
) -> DynamicOverload[[], typing.NoReturn]:
    dp = multimethod.multidispatch(dummy)

    dp.__name__ = name
    old_register = dp.register

    def _new_register(func: typing.Callable[P, R]) -> typing.Callable[P, R]:
        for dec in decs:
            func = dec(func)
        return old_register(func)

    dp.register = _new_register  # type: ignore
    return DynamicOverload(dp=dp)
