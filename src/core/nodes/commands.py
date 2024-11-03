from __future__ import annotations

import attrs

from . import base, procedure

attrs_frozen = attrs.frozen(kw_only=True)


@attrs_frozen
class Decrement(base.Node):
    """
    Token for decrementing the LAST_OWNER memory cell in BrainFuck.

    It decreases the value at the LAST_OWNER position by 1. Represented by '-' in BrainFuck.
    """


@attrs_frozen
class Increment(base.Node):
    """
    Token for incrementing the LAST_OWNER memory cell in BrainFuck.

    It increases the value at the LAST_OWNER position by 1. Represented by '+' in BrainFuck.
    """


@attrs_frozen
class Display(base.Node):
    """
    Token for outputting the value of the LAST_OWNER memory cell in BrainFuck.

    Outputs the ASCII character of the LAST_OWNER cell's value. Represented by '.' in BrainFuck.
    """


@attrs_frozen
class Input(base.Node):
    """
    Token for input in BrainFuck.

    Accepts a single ASCII character as input and stores it in the LAST_OWNER cell. Represented by ',' in BrainFuck.
    """


@attrs_frozen
class Loop(base.Node):
    """
    Token marking the brainfuck loop.

    Loop continues while the LAST_OWNER cell's value is non-zero. Represented by '[' in BrainFuck.
    """

    proc: procedure.Procedure


@attrs_frozen
class Clear(base.Node):
    """
    Token representing a clear base.Node in BrainFuck.

    Sets the value of the LAST_OWNER cell to zero. Represented by '[-]' as syntactic sugar in BrainFuck.
    """
