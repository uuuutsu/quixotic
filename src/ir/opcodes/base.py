import typing

import attrs

from src.common import tools
from src.ir import types


@attrs.frozen
@tools.impl(types.OpcodeType)
class BaseOpcode(metaclass=tools.FlyweightMeta):
    __slots__: typing.ClassVar[tuple[str, ...]] = ()
    identity: typing.ClassVar[str]

    def __init_subclass__(cls, **kwargs: typing.Any) -> None:
        cls.identity = tools.camel_case_to_snake_case(cls.__name__)

    def get_attrs(self) -> dict[str, typing.Any]:
        return {attr: getattr(self, attr) for attr in type(self).__slots__ if not attr.startswith("_")}
