import typing

import multimethod

P = typing.ParamSpec("P")
R = typing.TypeVar("R")
DecRetType = typing.TypeVar("DecRetType")


def dp_factory(
    name: str,
    *,
    decs: list[typing.Callable[[typing.Callable[..., typing.Any]], typing.Callable[P, R]]],
) -> multimethod.multidispatch[DecRetType]:
    @multimethod.multidispatch
    def _handler() -> typing.NoReturn:
        raise RuntimeError("emmm. What the sigma?")

    _handler.__name__ = name
    old_register = _handler.register

    def _new_register(func: typing.Callable[P, R]) -> typing.Callable[P, R]:
        for dec in decs:
            func = dec(func)
        return old_register(func)

    _handler.register = _new_register  # type: ignore
    return typing.cast(multimethod.multidispatch[DecRetType], _handler)
