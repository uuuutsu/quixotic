from __future__ import annotations

import typing

import attrs

from src.common import exceptions

from . import check


class IRError(exceptions.QuixoticError): ...


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
