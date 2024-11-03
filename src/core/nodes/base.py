from __future__ import annotations

import attrs

from src.core import types

CURRENT = object()


@attrs.frozen
class Node:
    owner: types.Owner = CURRENT
