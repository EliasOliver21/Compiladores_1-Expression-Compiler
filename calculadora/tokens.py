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

