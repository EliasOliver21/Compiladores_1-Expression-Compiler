from .tokens import TokenType
from .ast import ASTNode, NumberNode, BinOpNode

class Interpreter:
    def visit(self, node: ASTNode):
        """Método 'dispatcher' que chama o método de visita correto"""
        method_name = f'visit{type(node).name}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    