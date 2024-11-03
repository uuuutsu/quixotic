from __future__ import annotations

import attrs

from . import types

LAST_OWNER = object()


@attrs.frozen
class Node:
    owner: types.OwnerType = LAST_OWNER
