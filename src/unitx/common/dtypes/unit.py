import attrs

from . import base


@attrs.frozen(kw_only=True)
class Unit(base.DType): ...
