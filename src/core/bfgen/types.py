import io
import typing

type CodeType = io.StringIO


class PointerType(typing.Protocol):
    position: int
    def move(self, __pos: int) -> None: ...
