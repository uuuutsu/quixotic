import attrs

from . import base, types, utils

attrs_frozen = attrs.frozen(kw_only=True)


@attrs_frozen
class CompilerInjection(base.Node):
    """
    A class representing a compiler injection token in the compiler.
    """

    value: str = ""
    end_owner: types.OwnerType = base.CURRENT


@attrs_frozen
class CommentInjection(CompilerInjection):
    """
    A subclass of 'CompilerInjection' specifically for injecting comments into the compiler output.
    """

    value: str = attrs.field(validator=utils.check_injection_safety_attrs, default="")
    owner: types.OwnerType = attrs.field(init=False, default=base.CURRENT)
    end_owner: types.OwnerType = attrs.field(init=False, default=base.CURRENT)


@attrs_frozen
class CodeInjection(CompilerInjection):
    """
    A class for code injection tokens, inheriting from 'CompilerInjection'.

    This token has been inherited, to possibly be extended with checks and more functionality in the future.
    """
