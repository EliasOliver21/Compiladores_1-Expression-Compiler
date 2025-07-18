from enum import Enum

class TokenType(Enum):
    # Tipos de token
    INTEGER = 'INTEGER'
    PLUS    = 'PLUS'
    MINUS   = 'MINUS'
    MUL     = 'MUL'
    DIV     = 'DIV'
    LPAREN  = 'LPAREN'  
    RPAREN  = 'RPAREN'  
    EOF     = 'EOF'

class Token:
    """
    Representa um token, a menor unidade de significado.
    Ex: Token(TokenType.INTEGER, 10)
    """
    def __init__(self, type: TokenType, value: any = None):
        self.type = type
        self.value = value

    def __repr__(self):
        """Representação em string para facilitar a depuração."""
        return f'Token({self.type.name}, {repr(self.value)})'