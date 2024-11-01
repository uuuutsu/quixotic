import typing

import pytest

from src.widex.common import dtypes


def test_same_constant_state() -> None:
    const1 = dtypes.Constant(value=1)
    const2 = dtypes.Constant(value=1)
    assert const1 is const2


def test_diff_constant_state() -> None:
    const1 = dtypes.Constant(value=1)
    const2 = dtypes.Constant(value=2)
    assert const1 is not const2


def test_unit_hashability() -> None:
    unit = dtypes.Unit()
    assert isinstance(unit, typing.Hashable)


def test_array_creation_correct() -> None:
    arr = dtypes.Array(size=10, granularity=1)
    assert isinstance(arr, typing.Hashable)


def test_array_incorrect_creation() -> None:
    with pytest.raises(Exception) as _:
        dtypes.Array(size=-1)

    with pytest.raises(Exception) as _:
        dtypes.Array(size=10, granularity=-1)
