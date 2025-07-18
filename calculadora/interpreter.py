from .tokens import TokenType
from .ast import ASTNode, NumberNode, BinOpNode

class Interpreter:
    def visit(self, node: ASTNode):
        """Método 'dispatcher' que chama o método de visita correto"""
        method_name = f'visit{type(node).name}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: ASTNode):
        raise NotImplementedError(f"Nenhum método visit{type(node).name} definido")

    def _visit_NumberNode(self, node: NumberNode):
        """Visita um nó de número."""
        return node.value

    def _visit_BinOpNode(self, node: BinOpNode):
        """Visita um nó de operação binária"""
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)

        if node.op.type == TokenType.PLUS:
            return left_val + right_val
        if node.op.type == TokenType.MINUS:
            return left_val - right_val
        if node.op.type == TokenType.MUL:
            return left_val * right_val
        if node.op.type == TokenType.DIV:
            # Evitar divisão por zero
            if right_val == 0:
                raise ZeroDivisionError("Divisão por zero")
            return left_val / right_val