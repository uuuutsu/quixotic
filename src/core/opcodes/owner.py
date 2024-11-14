from __future__ import annotations

import typing


class OwnerType(typing.Hashable, typing.Protocol): ...


CURRENT_OWNER: typing.Final[OwnerType] = object()
