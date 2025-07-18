from .tokens import TokenType
from .ast import NumberNode, BinOpNode
from .lexer import Lexer

class Parser:
    def init(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def _eat(self, token_type: TokenType):
        """Consome o token atual se for do tipo esperado"""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise SyntaxError(f"Erro de sintaxe, esperado {token_type}, mas encontrou {self.current_token.type}")

    def _factor(self) -> BinOpNode | NumberNode:
        """Regra 'factor': trata números e os parênteses"""
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self._eat(TokenType.INTEGER)
            return NumberNode(token)
        elif token.type == TokenType.LPAREN:
            self._eat(TokenType.LPAREN)
            node = self._expr()
            self._eat(TokenType.RPAREN)
            return node
        raise SyntaxError("Fator inválido")

    def _term(self) -> BinOpNode | NumberNode:
        """Regra 'term': trata multiplicação e divisão"""
        node = self._factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            op = self.current_token
            self._eat(op.type)
            right = self._factor()
            node = BinOpNode(left=node, op=op, right=right)
        return node

    def _expr(self) -> BinOpNode | NumberNode:
        """Regra 'expr': trata soma e subtração (a regra principal)"""
        node = self._term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            self._eat(op.type)
            right = self._term()
            node = BinOpNode(left=node, op=op, right=right)
        return node

    def parse(self):
        """Inicia a análise e retorna a raiz da AST"""
        return self._expr()