import pytest

from src.ir import check_arg
from src.ir import exceptions as exc


def test_check_arg_with_callable_check() -> None:
    def check(kwargs: dict[str, int]) -> bool:
        return kwargs["x"] > 0

    @check_arg(check)
    def func(x: int) -> int:
        return x * 2

    assert func(5) == 10

    with pytest.raises(exc.CheckArgError):
        func(-3)


def test_check_arg_with_string_check() -> None:
    @check_arg("x > 0")
    def func(x: int) -> int:
        return x * 2

    assert func(5) == 10

    with pytest.raises(exc.CheckArgError):
        func(-3)


def test_check_arg_with_code_object_check() -> None:
    check_code = compile("x > 0", "<string>", "eval")

    @check_arg(check_code)
    def func(x: int) -> int:
        return x * 2

    assert func(5) == 10

    with pytest.raises(exc.CheckArgError):
        func(-3)


def test_check_arg_with_multiple_args() -> None:
    @check_arg("a < b")
    def func(a: int, b: int) -> int:
        return a + b

    assert func(1, 2) == 3

    with pytest.raises(exc.CheckArgError):
        func(3, 2)


def test_check_arg_with_kwargs() -> None:
    @check_arg("x == y")
    def func(x: int, y: int) -> int:
        return x * y

    assert func(2, 2) == 4

    with pytest.raises(exc.CheckArgError):
        func(2, 3)


def test_check_arg_with_default_args() -> None:
    @check_arg("x > 0")
    def func(x: int = 1) -> int:
        return x * 2

    assert func() == 2
    assert func(3) == 6

    with pytest.raises(exc.CheckArgError):
        func(0)


def test_check_arg_with_var_args() -> None:
    @check_arg("all(i > 0 for i in args)")
    def func(*args: int) -> int:
        return sum(args)

    assert func(1, 2, 3) == 6

    with pytest.raises(exc.CheckArgError):
        func(1, -2, 3)


def test_check_arg_with_var_kwargs() -> None:
    check = 'len(kwargs) == 2 and kwargs["x"] == kwargs["y"]'

    @check_arg(check)
    def func(**kwargs: int) -> int:
        return kwargs["x"] + kwargs["y"]

    assert func(x=2, y=2) == 4

    with pytest.raises(exc.CheckArgError):
        func(x=2, y=3)
