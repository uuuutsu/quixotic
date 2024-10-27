import attrs

from . import base


@attrs.frozen(kw_only=True)
class Array(base.BaseDType):
    size: int
    granularity: int = 1
