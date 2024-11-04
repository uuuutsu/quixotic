from __future__ import annotations

import typing

import attrs

from . import types

LAST_OWNER: typing.Final[object] = object()


@attrs.frozen
class Node:
    owner: types.OwnerType = LAST_OWNER
