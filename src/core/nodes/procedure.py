from __future__ import annotations

import typing

import attrs

from . import base


@attrs.frozen(kw_only=True)
class Procedure(base.Node):
    nodes: typing.Sequence[base.Node]
