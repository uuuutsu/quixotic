import abc
import typing

from src.widex.common import opcodes


class VisitorType(typing.Protocol):
    @abc.abstractmethod
    def visit(self, procedure: opcodes.ProcedureType) -> None:
        raise NotImplementedError

