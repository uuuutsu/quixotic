import abc

from src import ir
from src.ir import types

from . import dtypes


class Visitor[T](ir.Visitor[T]):
    @abc.abstractmethod
    def decrement(self, owner: dtypes.OwnerType) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def increment(self, owner: dtypes.OwnerType) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def output(self, owner: dtypes.OwnerType) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def input(self, owner: dtypes.OwnerType) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def loop(self, owner: dtypes.OwnerType, opcode: types.OpcodeType) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self, owner: dtypes.OwnerType) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def comment(self, value: str) -> None:
        raise NotImplementedError
