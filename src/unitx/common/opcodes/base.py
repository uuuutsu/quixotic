from __future__ import annotations

import typing

from src.unitx.common import dtypes


class OpcodeMeta(type):
    def __new__(
        cls: type[OpcodeMeta],
        name: str,
        bases: tuple[type[typing.Any], ...],
        classdict: dict[str, typing.Any],
        **kwargs: typing.Any,
    ) -> OpcodeMeta:
        classdict.setdefault("__attrs__", classdict.get("__slots__", {}))
        return super().__new__(cls, name, bases, classdict, **kwargs)


class Opcode(metaclass=OpcodeMeta):
    __attrs__: typing.ClassVar[tuple[str, ...]] = ()

    def get_attrs(self) -> tuple[dtypes.DType, ...]:
        return tuple(getattr(self, name) for name in self.__attrs__)

    @property
    def name(self) -> str:
        return type(self).__name__
