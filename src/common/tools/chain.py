from __future__ import annotations

import typing

import attrs

from src.common import interfaces


@attrs.frozen
class BaseChain[I, R](interfaces.ChainType[I, R]):
    factory: typing.Callable[[I], R]

    def __call__(self, data: I) -> R:
        return self.factory(data)

    def __or__[C](self, factory: interfaces.ChainType[R, C]) -> BaseChain[I, C]:
        def _wrapper(data: I) -> C:
            return factory(self(data))

        return BaseChain(_wrapper)
