from __future__ import annotations

import attrs

from . import base, procedure

attrs_frozen = attrs.frozen(kw_only=True)


@attrs_frozen
class Decrement(base.Node):
    """
    Token for decrementing the current memory cell in BrainFuck.

    It decreases the value at the current position by 1. Represented by '-' in BrainFuck.
    """


@attrs_frozen
class Increment(base.Node):
    """
    Token for incrementing the current memory cell in BrainFuck.

    It increases the value at the current position by 1. Represented by '+' in BrainFuck.
    """


@attrs_frozen
class Display(base.Node):
    """
    Token for outputting the value of the current memory cell in BrainFuck.

    Outputs the ASCII character of the current cell's value. Represented by '.' in BrainFuck.
    """


@attrs_frozen
class Input(base.Node):
    """
    Token for input in BrainFuck.

    Accepts a single ASCII character as input and stores it in the current cell. Represented by ',' in BrainFuck.
    """


@attrs_frozen
class Loop(base.Node):
    """
    Token marking the brainfuck loop.

    Loop continues while the current cell's value is non-zero. Represented by '[' in BrainFuck.
    """

    proc: procedure.Procedure


@attrs_frozen
class Clear(base.Node):
    """
    Token representing a clear base.Node in BrainFuck.

    Sets the value of the current cell to zero. Represented by '[-]' as syntactic sugar in BrainFuck.
    """
