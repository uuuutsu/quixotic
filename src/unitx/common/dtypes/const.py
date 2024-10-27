import attrs

from src.tools import cls

from . import base


@attrs.frozen(kw_only=True)
class Constant[T](base.BaseDType, metaclass=cls.FlyweightMeta):
    value: T
