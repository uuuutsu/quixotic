import attrs

from src.core import types

from . import base, utils

attrs_frozen = attrs.frozen(kw_only=True)


@attrs_frozen
class CompilerInjection(base.Node):
    """
    A class representing a compiler injection token in the compiler.
    """

    value: str = ""
    end_owner: types.Owner | None = None

    def __attrs_post_init__(self) -> None:
        if self.end_owner is None:
            object.__setattr__(self, "end_owner", self.owner)


@attrs_frozen
class CommentInjection(base.Node):
    """
    A subclass of 'CompilerInjection' specifically for injecting comments into the compiler output.
    """

    value: str = attrs.field(validator=utils.check_injection_safety_attrs, default="")
    owner: types.Owner | None = attrs.field(init=False, default=None)
    end_owner: types.Owner | None = attrs.field(init=False, default=None)


@attrs_frozen
class CodeInjection(base.Node):
    """
    A class for code injection tokens, inheriting from 'CompilerInjection'.

    This token has been inherited, to possibly be extended with checks and more functionality in the future.
    """
