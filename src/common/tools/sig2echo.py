from __future__ import annotations

import functools
import inspect
import typing

P = typing.ParamSpec("P")


def signature_to_echo(func: typing.Callable[P, typing.Any]) -> typing.Callable[P, dict[str, typing.Any]]:
    @functools.wraps(func)
    def _echo(*args: P.args, **kwargs: P.kwargs) -> dict[str, typing.Any]:
        bounded_signature = inspect.signature(func).bind(*args, **kwargs)
        bounded_signature.apply_defaults()
        return typing.cast(dict[str, typing.Any], bounded_signature.arguments)

    return _echo
