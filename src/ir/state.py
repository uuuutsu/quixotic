from . import types


class StateBase[K: types.DType, V](dict[K, V]): ...
