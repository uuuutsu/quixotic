from src.ir import types


class State[K: types.DType, V](dict[K, V]): ...
