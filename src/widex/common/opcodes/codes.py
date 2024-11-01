import abc
import typing

from src.widex.common import dtypes

from .types import ProcedureType
from .utils import opcode_from_sig


class Printable(typing.Protocol):
    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


type Wide = tuple[dtypes.Unit, ...]
type Array = dtypes.Array
type Const[T] = dtypes.Constant[T]
type Opt[T] = typing.Optional[T]

type Arg[T] = Wide | Const[T]
type Res = Wide

type Index = Wide | Const[int]
type StoreArg = Wide | Const[int]
type LoadArr = Array | Const[typing.Sequence[int]]
type LoadRes = Wide

type Procedure = ProcedureType
type SwitchCases = dict[Arg[int], Procedure]

type Scale = int
type MoveRes = tuple[tuple[Res, Scale], ...]


@opcode_from_sig
def add(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def sub(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def mul(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def lshift(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def rshift(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def div(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def mod(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def divmod(left: Arg[int], right: Arg[int], quot: Opt[Res], rem: Opt[Res]) -> None: ...


@opcode_from_sig
def and_(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def or_(left: Arg[int], right: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def not_(left: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def xor(left: Arg[int], right: Arg[int], target: Res) -> None: ...


@opcode_from_sig
def arr_move(idx: Index, array: Array, rel: Index) -> None: ...
@opcode_from_sig
def arr_store(idx: Index, array: Array, value: StoreArg) -> None: ...
@opcode_from_sig
def arr_load(idx: Index, array: LoadArr, target: LoadRes) -> None: ...


@opcode_from_sig
def callz(value: Wide, if_: Procedure, else_: Procedure) -> None: ...
@opcode_from_sig
def calleq(left: Wide, right: Arg[int], if_: Procedure, else_: Procedure) -> None: ...
@opcode_from_sig
def callneq(left: Wide, right: Arg[int], if_: Procedure, else_: Procedure) -> None: ...
@opcode_from_sig
def callge(left: Wide, right: Arg[int], if_: Procedure, else_: Procedure) -> None: ...
@opcode_from_sig
def callgt(left: Wide, right: Arg[int], if_: Procedure, else_: Procedure) -> None: ...
@opcode_from_sig
def callle(left: Wide, right: Arg[int], if_: Procedure, else_: Procedure) -> None: ...
@opcode_from_sig
def calllt(left: Wide, right: Arg[int], if_: Procedure, else_: Procedure) -> None: ...
@opcode_from_sig
def switch(value: Wide, cases: SwitchCases, else_: Procedure) -> None: ...


@opcode_from_sig
def assign(value: Arg[int], target: Res) -> None: ...
@opcode_from_sig
def copy(value: Wide, target: Res) -> None: ...
@opcode_from_sig
def move(value: Wide, target: MoveRes) -> None: ...


@opcode_from_sig
def input(target: Res) -> None: ...
@opcode_from_sig
def output(argument: Arg[Printable]) -> None: ...


@opcode_from_sig
def alloc(value: Wide | Array) -> None: ...
@opcode_from_sig
def free(value: Wide | Array) -> None: ...
