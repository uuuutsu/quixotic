import typing

from src.ir import types


class VisitorBase[T](types.VisitorType[T]):
    def visit(self, opcode: types.OpcodeType) -> T:
        executor = getattr(self, opcode.identity, None)
        if not (executor and callable(executor)):
            raise AttributeError(f"No executor found for: {opcode}")

        return typing.cast(T, executor(**opcode.get_attrs()))
