import attrs

from src.ir import types

from . import base


@attrs.frozen
class Procedure(base.BaseOpcode):
    opcodes: types.OpcodeType
