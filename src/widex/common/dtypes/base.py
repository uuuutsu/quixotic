import attrs

from src.common import tools


@attrs.frozen
class AbstractDType:
    name: str | None = None
    _id: int = attrs.field(init=False, factory=tools.generate_unique_id)

    def __hash__(self) -> int:
        return self._id
