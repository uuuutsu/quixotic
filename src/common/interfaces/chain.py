from __future__ import annotations

import abc
import typing


class ChainType[I, O](typing.Protocol):
    @abc.abstractmethod
    def __call__(self, __data: I) -> O:
        raise NotImplementedError

    @abc.abstractmethod
    def __or__[C](self, __func: ChainType[O, C]) -> ChainType[I, C]:
        raise NotImplementedError
