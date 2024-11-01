from __future__ import annotations

import typing

from src.widex.common import dtypes


class Opcode:
    __slots__ = ()
    __attrs__: typing.ClassVar[tuple[str, ...]] = ()

    def get_attrs(self) -> dict[str, dtypes.DType]:
        return {name: getattr(self, name) for name in self.__attrs__}

    @property
    def identity(self) -> typing.Hashable:
        return type(self).__name__
