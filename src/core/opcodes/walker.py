import abc

from src import ir

from . import owner


class Walker(ir.WalkerBase):
    @abc.abstractmethod
    def decrement(self, owner: owner.OwnerType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def increment(self, owner: owner.OwnerType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def output(self, owner: owner.OwnerType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def input(self, owner: owner.OwnerType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def loop(self, owner: owner.OwnerType, proc: ir.ProcedureType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self, owner: owner.OwnerType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def compiler_injection(self, value: str, end_owner: owner.OwnerType = owner.CURRENT_OWNER) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def comment_injection(
        self,
        value: str,
        owner: owner.OwnerType = owner.CURRENT_OWNER,
        end_owner: owner.OwnerType = owner.CURRENT_OWNER,
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def code_injection(self, value: str = "", end_owner: owner.OwnerType = owner.CURRENT_OWNER) -> None:
        raise NotImplementedError
