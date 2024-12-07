import attrs

from src.common import tools

from . import base


@attrs.frozen(kw_only=True)
class Const[T](base.DTypeBase, metaclass=tools.FlyweightMeta):
    value: T
