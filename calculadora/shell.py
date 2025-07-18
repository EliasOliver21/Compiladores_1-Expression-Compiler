from calculadora.lexer import Lexer
from calculadora.parser import Parser
from calculadora.interpreter import Interpreter

def main():
    print("Calculadora de Expressões v0.1")
    print("Digite 'sair' para fechar.")

    while True:
        try:
            text = input("calc > ")
            if text.strip().lower() == 'sair':
                break
            if not text:
                continue

            lexer = Lexer(text)
            parser = Parser(lexer)
            tree = parser.parse()

            interpreter = Interpreter()
            result = interpreter.visit(tree)

            print(result)

        except Exception as e:
            print(f"Erro: {e}")

if name == 'main':
    main()