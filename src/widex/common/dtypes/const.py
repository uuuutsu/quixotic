import attrs

from src.tools import cls

from . import base


@attrs.frozen(kw_only=True)
class Const[T](base.AbstractDType, metaclass=cls.FlyweightMeta):
    value: T
