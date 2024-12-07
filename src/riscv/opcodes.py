import attrs

from . import dtypes


@attrs.frozen
class Add:
    left: dtypes.Reg
    right: dtypes.Reg
    target: dtypes.Reg
