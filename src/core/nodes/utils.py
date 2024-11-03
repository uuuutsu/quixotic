from __future__ import annotations

import re
import typing

from src.core import exceptions


def check_injection_safety_attrs(inst: typing.Any, attr: typing.Any, info: str) -> None:
    check_injection_safety(info)


def check_injection_safety(info: str) -> None:
    """
    Validate the given string for BrainFuck command character injection.

    This function checks if the `info` string contains any BrainFuck command characters.
    If such characters are detected, a `CodeSemanticsViolationError` is raised.
    """
    match = re.match(r".*([,.><\[\]+-]).*", info)
    if match is not None:
        raise exceptions.CodeSemanticsViolationError(info, match.start(1))
