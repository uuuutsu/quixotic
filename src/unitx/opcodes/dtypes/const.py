import attrs

from src import ir
from src.common import tools


@attrs.frozen(kw_only=True)
class Const[T](ir.DTypeBase, metaclass=tools.FlyweightMeta):
    value: T
