from .tokens import Token

class ASTNode:
    """Classe base para todos os nós da árvore."""
    pass

class NumberNode(ASTNode):
    """Nó para um número."""
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

class BinOpNode(ASTNode):
    """Nó para uma operação binária (ex: 1 + 2)."""
    def __init__(self, left: ASTNode, op: Token, right: ASTNode):
        self.left = left
        self.op = op
        self.right = right