from __future__ import annotations

import typing

from src import ir
from src.unitx.prelude import dtypes


class State(ir.State[dtypes.Unit | dtypes.Array, int | list[int]]):
    if typing.TYPE_CHECKING:

        @typing.overload  # type: ignore
        def __getitem__(self, idx: dtypes.Unit, /) -> int: ...
        @typing.overload
        def __getitem__(self, idx: dtypes.Array, /) -> list[int]: ...
        def __getitem__(self, idx: dtypes.Array | dtypes.Unit, /) -> int | list[int]:
            raise NotImplementedError

        @typing.overload  # type: ignore
        def __setitem__(self, idx: dtypes.Unit, value: int, /) -> None: ...
        @typing.overload
        def __setitem__(self, idx: dtypes.Array, value: list[int], /) -> None: ...
        def __setitem__(self, idx: dtypes.Array | dtypes.Unit, value: int | list[int], /) -> None:
            raise NotImplementedError
