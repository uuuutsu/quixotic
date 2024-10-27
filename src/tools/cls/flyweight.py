from __future__ import annotations

import abc
import typing


class FlyweightStateType(typing.Protocol):
    @abc.abstractmethod
    def __call__(*__args: typing.Any, **__kwargs: typing.Any) -> typing.Hashable:
        raise NotImplementedError


def _dummy_factory(*args: typing.Any, **kwargs: typing.Any) -> str:
    return f"{args}_{kwargs}"


@typing.final
class FlyweightMeta(abc.ABCMeta):
    __flyweights__: dict[typing.Hashable, FlyweightMeta]
    __state_factory__: FlyweightStateType

    def __init__(
        cls: FlyweightMeta,
        name: str,
        bases: tuple[type[typing.Any], ...],
        classdict: dict[str, typing.Any],
        state_factory: FlyweightStateType = _dummy_factory,
        **kwargs: typing.Any,
    ) -> None:
        super().__init__(name, bases, classdict, **kwargs)
        cls.__flyweights__ = {}
        cls.__state_factory__ = state_factory

    def __call__(cls: FlyweightMeta, *args: typing.Any, **kwargs: typing.Any) -> FlyweightMeta:
        state = cls.__state_factory__(*args, **kwargs)
        if state in cls.__flyweights__:
            return cls.__flyweights__[state]
        return cls.__flyweights__.setdefault(state, super().__call__(*args, **kwargs))
