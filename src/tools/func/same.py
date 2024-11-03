import functools
import typing

P = typing.ParamSpec("P")
R = typing.TypeVar("R")


def same_as(func: typing.Callable[P, R], /) -> typing.Callable[[typing.Callable[P, R]], typing.Callable[P, R]]:
    @functools.wraps(func)
    def _wrapper(new_func: typing.Callable[P, R], /) -> typing.Callable[P, R]:
        return new_func

    return _wrapper
