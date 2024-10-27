import attrs

from . import base


@attrs.frozen(kw_only=True)
class Array(base.DType):
    size: int
    granularity: int = 1
