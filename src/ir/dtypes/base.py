import attrs

from src.common import tools


@attrs.frozen(hash=False, repr=False)
class DTypeBase:
    name: str | None = None
    id: int = attrs.field(factory=tools.generate_unique_id)

    def __hash__(self) -> int:
        return self.id

    def __repr__(self) -> str:
        return f"{type(self).__name__}( {self.name or self.id} )"
