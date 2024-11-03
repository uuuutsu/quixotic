import pytest

from src import core

_OwnerPlaceholder = 0


def test_compiler_injection_initialization() -> None:
    node = core.CompilerInjection(value="++")
    assert node.value == "++"


def test_compiler_injection_default_exit() -> None:
    node = core.CodeInjection(value="+-", owner=1)
    assert node.end_owner is core.LAST_OWNER


def test_comment_injection_attributes() -> None:
    comment = core.CommentInjection(value="This is a comment")
    assert comment.owner is core.LAST_OWNER
    assert comment.end_owner is core.LAST_OWNER


def test_check_injection_safety_valid() -> None:
    try:
        core.CommentInjection(value="This is safe")
    except Exception as exc:
        pytest.fail(f"Unexpected `{exc}` error for safe string")


def test_check_injection_safety_invalid() -> None:
    with pytest.raises(core.CodeSemanticsViolationError):
        core.CommentInjection(value="++[>.<]")


def test_check_injection_safety_error_details() -> None:
    with pytest.raises(core.CodeSemanticsViolationError) as exc_info:
        core.CommentInjection(value="++[>.<]")

    assert "++[>.<]" in str(exc_info.value)
