import typing

import attrs

from src.ir.exceptions import IRError

from . import check


@attrs.define(str=False)
class CheckArgError(IRError):
    func: typing.Callable[..., typing.Any]
    check: check.CheckType
    args: tuple[typing.Any, ...]
    kwargs: dict[str, typing.Any]

    def __str__(self) -> str:
        return (
            f"During call to {self.func!r}, check: {self.check!r} failed.\n\n"
            f"\t\tArgs: {self.args}\n"
            f"\t\tKwargs: {self.kwargs}"
        )
