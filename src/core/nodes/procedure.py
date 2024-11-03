from __future__ import annotations

import typing

from . import base, utils


@utils.attrs_frozen
class Procedure(base.Node):
    nodes: typing.Sequence[base.Node]
