import attrs

from src import ir
from src.core import opcodes


@attrs.frozen
class Emulator(opcodes.Walker):
    state: dict[opcodes.OwnerType, int] = attrs.field(factory=dict)

    def decrement(self, owner: opcodes.OwnerType) -> None:
        if self.state.setdefault(owner, 0) == 0:
            self.state[owner] = 256
        self.state[owner] -= 1

    def increment(self, owner: opcodes.OwnerType) -> None:
        if self.state.setdefault(owner, 255) == 255:
            self.state[owner] = -1
        self.state[owner] += 1

    def output(self, owner: opcodes.OwnerType) -> None:
        print(chr(self.state[owner]), end="")

    def input(self, owner: opcodes.OwnerType) -> None:
        self.state[owner] = ord(input(":")[0]) % 255

    def loop(self, owner: opcodes.OwnerType, proc: ir.ProcedureType) -> None:
        codes = iter(proc)
        while self.state[owner] and (opcode := next(codes)):
            self.step(opcode)

    def clear(self, owner: opcodes.OwnerType) -> None:
        self.state[owner] = 0

    def compiler_injection(self, value: str, end_owner: opcodes.OwnerType = opcodes.CURRENT_OWNER) -> None:
        raise NotImplementedError

    def comment_injection(
        self,
        value: str,
        owner: opcodes.OwnerType = opcodes.CURRENT_OWNER,
        end_owner: opcodes.OwnerType = opcodes.CURRENT_OWNER,
    ) -> None:
        raise NotImplementedError

    def code_injection(self, value: str = "", end_owner: opcodes.OwnerType = opcodes.CURRENT_OWNER) -> None:
        raise NotImplementedError
