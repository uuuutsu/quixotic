from __future__ import annotations

import typing

from src.ir import types


class OwnerType(types.DType, typing.Hashable, typing.Protocol): ...


CURRENT_OWNER: typing.Final[OwnerType] = object()
