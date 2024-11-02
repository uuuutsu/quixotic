from __future__ import annotations

import typing

import attrs

from . import base, unit


def _to_units(units: tuple[unit.Unit, ...] | int) -> tuple[unit.Unit, ...]:
    if isinstance(units, tuple):
        return units

    return tuple(unit.Unit(f"_{idx}") for idx in range(units))


@attrs.frozen(kw_only=True)
class Wide(base.AbstractDType):
    _units: tuple[unit.Unit, ...] = attrs.field(converter=_to_units)

    def __iter__(self) -> typing.Iterator[unit.Unit]:
        return self._units.__iter__()

    @typing.overload
    def __getitem__(self, idx: int) -> unit.Unit: ...
    @typing.overload
    def __getitem__(self, idx: slice) -> Wide: ...
    def __getitem__(self, idx: int | slice) -> unit.Unit | Wide:
        if isinstance(idx, int):
            return self._units[idx]
        return type(self)(units=self._units[idx])

    def __len__(self) -> int:
        return len(self._units)
