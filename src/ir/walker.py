from . import types


class WalkerBase(types.WalkerType):
    def walk(self, proc: types.ProcedureType) -> None:
        for opcode in proc:
            executor = getattr(self, opcode.identity, None)
            if not (executor and callable(executor)):
                raise AttributeError(f"No executor found for: {opcode}")

            executor(**opcode.get_attrs())
