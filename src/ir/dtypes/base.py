from src.common import tools
from src.ir import types


@tools.impl(types.DType)
class DTypeBase:
    __slots__ = (
        "id",
        "name",
    )

    def __init__(self, name: str | None = None, id: int | None = None) -> None:
        self.name = name
        self.id = id or tools.generate_unique_id()

    def __hash__(self) -> int:
        return self.id

    def __repr__(self) -> str:
        return f"{type(self).__name__}( {self.name or self.id} )"
