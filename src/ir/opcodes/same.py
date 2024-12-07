import typing

Inst = typing.TypeVar("Inst")
P = typing.ParamSpec("P")
R = typing.TypeVar("R")


def same_as(
    _sig: typing.Callable[P, R], /
) -> (
    typing.Callable[[typing.Callable[P, R]], typing.Callable[P, R]]
    | typing.Callable[
        [typing.Callable[typing.Concatenate[Inst, P], R]], typing.Callable[typing.Concatenate[Inst, P], R]
    ]
):
    return lambda func: func
