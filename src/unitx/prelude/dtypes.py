__all__ = (
    "Const",
    "Array",
    "Unit",
)

import attrs
from attrs import validators

from src import ir
from src.ir.dtypes import Const


@attrs.frozen(kw_only=True)
class Array(ir.DTypeBase):
    size: int = attrs.field(
        validator=validators.gt(0),
    )
    granularity: int = attrs.field(
        validator=validators.gt(0),
        default=1,
    )


@attrs.frozen(kw_only=True)
class Unit(ir.DTypeBase): ...
