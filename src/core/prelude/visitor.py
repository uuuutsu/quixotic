import abc

from src import ir

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
    def loop(self, owner: dtypes.OwnerType, opcode: ir.Opcode) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self, owner: dtypes.OwnerType) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def comment(
        self,
        value: str,
        owner: dtypes.OwnerType = dtypes.CURRENT_OWNER,
        end_owner: dtypes.OwnerType = dtypes.CURRENT_OWNER,
    ) -> None:
        raise NotImplementedError
