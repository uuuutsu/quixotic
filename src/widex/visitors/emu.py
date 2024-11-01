import functools
import typing

from src.tools import generic
from src.widex.common import opcodes
from src.widex.common.dtypes import Array, Const, Wide
from src.widex.common.opcodes import ProcedureType

from . import types


class WideXEmulator(types.VisitorType):
    def visit(self, procedure: ProcedureType) -> None:
        for opcode in procedure:
            if not (func := getattr(self, opcode.identity, None)):
                raise AttributeError(f"Unknown opcode {opcode.identity}")
            if not callable(func):
                raise TypeError(f"Current implementation for {opcode.identity} is not callable. Ha?")

            func(*opcode.get_attrs())

    @functools.wraps(opcodes.add)
    def add(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.sub)
    def sub(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.mul)
    def mul(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.lshift)
    def lshift(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.rshift)
    def rshift(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.div)
    def div(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.mod)
    def mod(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.divmod)
    def divmod(self, left: Wide | Const[int], right: Wide | Const[int], quot: Wide = (), rem: Wide = ()) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.and_)
    def and_(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.or_)
    def or_(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.not_)
    def not_(self, left: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.xor)
    def xor(self, left: Wide | Const[int], right: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.arr_move)
    def arr_move(self, idx: Wide | Const[int], array: Array, rel: Wide | Const[int]) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.arr_store)
    def arr_store(self, idx: Wide | Const[int], array: Array, value: Wide | Const[int]) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.arr_load)
    def arr_load(self, idx: Wide | Const[int], array: Array | Const[typing.Sequence[int]], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.callz)
    def callz(self, value: Wide, if_: ProcedureType, else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.calleq)
    def calleq(self, left: Wide, right: Wide | Const[int], if_: ProcedureType, else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.callneq)
    def callneq(self, left: Wide, right: Wide | Const[int], if_: ProcedureType, else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.callge)
    def callge(self, left: Wide, right: Wide | Const[int], if_: ProcedureType, else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.callgt)
    def callgt(self, left: Wide, right: Wide | Const[int], if_: ProcedureType, else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.callle)
    def callle(self, left: Wide, right: Wide | Const[int], if_: ProcedureType, else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.calllt)
    def calllt(self, left: Wide, right: Wide | Const[int], if_: ProcedureType, else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.switch)
    def switch(self, value: Wide, cases: dict[Wide | Const[int], ProcedureType], else_: ProcedureType) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.assign)
    def assign(self, value: Wide | Const[int], target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.copy)
    def copy(self, value: Wide, target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.move)
    def move(self, value: Wide, target: tuple[tuple[Wide, int], ...]) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.input)
    def input(self, target: Wide) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.output)
    def output(self, argument: Wide | Const[generic.PrintableType]) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.alloc)
    def alloc(self, value: Wide | Array) -> None:
        raise NotImplementedError

    @functools.wraps(opcodes.free)
    def free(self, value: Wide | Array) -> None:
        raise NotImplementedError
