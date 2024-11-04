import abc

from src.common import interfaces, tools

from . import base, commands, injection, procedure


class AbstractVisitor(interfaces.VisitorType[base.Node], abc.ABC):
    @abc.abstractmethod
    def visit_decrement(self, node: commands.Decrement) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_increment(self, node: commands.Increment) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_output(self, node: commands.Output) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_input(self, node: commands.Input) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_loop(self, node: commands.Loop) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_clear(self, node: commands.Clear) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_compiler_injection(self, node: injection.CompilerInjection) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_comment_injection(self, node: injection.CommentInjection) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_code_injection(self, node: injection.CodeInjection) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_procedure(self, node: procedure.Procedure) -> None:
        raise NotImplementedError

    def visit(self, node: base.Node) -> None:
        name = tools.camel_case_to_snake_case(type(node).__name__.lower())
        method = getattr(self, f"visit_{name}", None)
        if not callable(method):
            raise NotImplementedError(f"No handler found for {name}")
        method(node)
