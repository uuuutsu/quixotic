from . import types


class StateBase[V](dict[types.DType, V]): ...
