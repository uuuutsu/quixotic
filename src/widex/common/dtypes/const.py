import attrs

from src.common import tools

from . import base


@attrs.frozen(kw_only=True)
class Const[T](base.AbstractDType, metaclass=tools.FlyweightMeta):
    value: T
