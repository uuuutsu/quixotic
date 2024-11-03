from __future__ import annotations

import attrs

from . import types

CURRENT = object()


@attrs.frozen
class Node:
    owner: types.OwnerType = CURRENT
