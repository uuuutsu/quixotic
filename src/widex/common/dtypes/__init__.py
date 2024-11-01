__all__ = (
    "DType",
    "Array",
    "Const",
    "Unit",
    "Wide",
)

import typing

from .array import Array
from .const import Const
from .types import DType
from .unit import Unit

type Wide = typing.Sequence[Unit]
