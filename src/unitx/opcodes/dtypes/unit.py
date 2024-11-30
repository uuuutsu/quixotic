import attrs

from src import ir


@attrs.frozen(kw_only=True)
class Unit(ir.DTypeBase): ...
