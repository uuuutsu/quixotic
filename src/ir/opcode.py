import typing

from src.common import tools

from . import types


class BaseOpcode[ArgType](types.OpcodeType):
    __slots__: typing.ClassVar[tuple[str, ...]] = ()

    def __init_subclass__(cls, **kwargs: typing.Any) -> None:
        cls.identity = tools.camel_case_to_snake_case(cls.__name__)

    def get_attrs(self) -> dict[str, ArgType]:
        return {attr: getattr(self, attr) for attr in type(self).__slots__}
