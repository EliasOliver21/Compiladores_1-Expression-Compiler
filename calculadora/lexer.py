from .tokens import Token, TokenType

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def _advance(self):
        """Avança o ponteiro 'pos' e atualiza 'current_char'."""
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def _skip_whitespace(self):
        """Pula espaços em branco."""
        while self.current_char is not None and self.current_char.isspace():
            self._advance()

    def _get_integer(self):
        """Lê um número inteiro da entrada."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self._advance()
        return int(result)

    def get_next_token(self) -> Token:
        """O coração do analisador léxico."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self._skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self._get_integer())

            if self.current_char == '+':
                self._advance()
                return Token(TokenType.PLUS)
            if self.current_char == '-':
                self._advance()
                return Token(TokenType.MINUS)
            if self.current_char == '*':
                self._advance()
                return Token(TokenType.MUL)
            if self.current_char == '/':
                self._advance()
                return Token(TokenType.DIV)
            if self.current_char == '(':
                self._advance()
                return Token(TokenType.LPAREN)
            if self.current_char == ')':
                self._advance()
                return Token(TokenType.RPAREN)

            raise ValueError(f"Caractere inválido: '{self.current_char}'")

        return Token(TokenType.EOF)