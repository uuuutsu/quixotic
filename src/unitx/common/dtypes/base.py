import attrs

from src.tools import func


@attrs.frozen
class BaseDType:
    name: str | None = None
    _id: int = attrs.field(init=False, factory=func.generate_unique_id)

    def __hash__(self) -> int:
        return self._id
