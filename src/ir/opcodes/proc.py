import typing

import attrs

from src.ir import types

from . import base


@attrs.frozen
class Procedure(base.Opcode):
    opcodes: typing.Sequence[types.Opcode]
