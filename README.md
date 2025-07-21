# Compilador de Expressões Aritméticas

## Integrantes

|Matrícula | Aluno |
| -- | -- |
| 22/1007958  |  Cláudio Henrique dos Santos Carvalho |
| 22/1007706  |  Elias Faria de Oliveira |

## Introdução

Este projeto implementa um interpretador para uma linguagem de expressões aritméticas simples, desenvolvido como trabalho final para a disciplina de Compiladores 1. O objetivo é demonstrar na prática as fases clássicas de um compilador: análise léxica, análise sintática, construção de uma representação intermediária (Árvore de Sintaxe Abstrata - AST) e a interpretação (execução) dessa árvore para produzir um resultado final.

A estratégia de implementação foi utilizar um **Analisador Sintático Descendente Recursivo** (*Recursive Descent Parser*), um algoritmo intuitivo que reflete diretamente a gramática da linguagem em sua estrutura de código.

### A Linguagem

A linguagem implementada permite a avaliação de expressões aritméticas contendo:

* **Sintaxe:**
    * Números inteiros (positivos).
    * Operadores de adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`).
    * Parênteses `()` para agrupamento e definição de precedência.
    * Espaços em branco são ignorados.

* **Semântica:**
    * As operações seguem a precedência matemática padrão: multiplicação e divisão são executadas antes de adição e subtração.
    * Parênteses forçam a avaliação da expressão interna antes de seu resultado ser usado em operações externas.

* **Exemplos de Comandos Válidos:**
    * `10 + 5`
    * `10 + 5 * 2` (Resultado: 20, devido à precedência)
    * `(10 + 5) * 2` (Resultado: 30, devido ao agrupamento)
    * `100 / (2 * (3 + 2)) - 1` (Resultado: 9.0)

## Instalação e Execução

O projeto é escrito em Python 3 e não possui dependências externas.

**Passos para executar:**

1.  Clone o repositório.
2.  Navegue até a pasta raiz do projeto.
3.  Execute o shell interativo com o seguinte comando:
    ```bash
    python shell.py
    ```
4.  Digite as expressões no prompt `calc > ` e pressione Enter para ver o resultado. Para sair, digite `sair`.

## Exemplos

A pasta `exemplos/` contém arquivos `.txt` com expressões de complexidade variada, demonstrando as capacidades da linguagem. Como a linguagem implementada é puramente aritmética, os exemplos focam em testar a robustez do analisador.

* `exemplo_simples.txt`: Uma operação básica de soma.
* `exemplo_precedencia.txt`: Testa a precedência da multiplicação sobre a adição.
* `exemplo_parenteses.txt`: Testa o agrupamento com parênteses.
* `exemplo_complexo.txt`: Uma expressão com múltiplos operadores e parênteses aninhados.

## Referências

Para o desenvolvimento deste projeto, foram utilizadas as seguintes referências:

1.  **Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools (2nd ed.)*.**
    * **Papel:** Conhecido como "Livro do Dragão", serviu como a principal referência teórica para entender os conceitos de cada fase do compilador, especialmente as gramáticas livres de contexto e a análise sintática.

2.  **Spivak, R. (2018). *Let's Build a Simple Interpreter*.**
    * **Papel:** Este tutorial online foi uma referência prática fundamental. A estrutura do nosso código (separação em Lexer, Parser, Interpreter) e a implementação do analisador descendente recursivo foram fortemente inspiradas na abordagem didática apresentada por Spivak.

3. **CRAFTING INTERPRETER**
    * **Papel:** (Crafting Interpreters)[https://craftinginterpreters.com/] contém tudo o que você precisa para implementar uma linguagem de script completa e eficiente.

## Estrutura do Código

O código-fonte está organizado em módulos, cada um responsável por uma fase ou componente específico do compilador, facilitando a compreensão e manutenção.

* `calculadora/tokens.py`: Define a `Enum` `TokenType` e a classe `Token`, que são as estruturas de dados para os tokens.
* `calculadora/ast.py`: Define as classes dos nós da Árvore Sintática Abstrata (`NumberNode`, `BinOpNode`), que formam a representação interna do código.
* `calculadora/lexer.py`: Contém a classe `Lexer`, responsável pela **Análise Léxica**. Ela transforma a string de entrada em uma sequência de tokens.
* `calculadora/parser.py`: Contém a classe `Parser`, responsável pela **Análise Sintática**. Ela consome os tokens do Lexer e constrói a AST.
* `calculadora/interpreter.py`: Contém a classe `Interpreter`, que realiza a **Análise Semântica** (implícita, durante a execução) e a **Geração de Código** (neste caso, a avaliação direta da AST para produzir um resultado numérico).
* `shell.py`: Ponto de entrada do programa, responsável pela interface com o usuário e por orquestrar a interação entre os componentes.

## Bugs, Limitações e Melhorias Futuras

* **Limitações Conhecidas:**
    * **Apenas Inteiros:** O lexer só reconhece números inteiros. Não há suporte para números de ponto flutuante.
    * **Sem Variáveis:** A linguagem não possui conceito de variáveis, atribuições ou estado. Cada cálculo é independente.
    * **Relatório de Erros:** O tratamento de erros é simples. Ele captura exceções e exibe uma mensagem, mas não informa a linha ou coluna exata onde o erro ocorreu.
    * **Divisão por Zero:** A divisão por zero é tratada, mas interrompe o cálculo com uma mensagem de erro, em vez de retornar um valor como `infinito`.

* **Melhorias Futuras:**
    * Adicionar suporte a números de ponto flutuante.
    * Implementar variáveis e uma Tabela de Símbolos para armazená-las.
    * Melhorar o sistema de relatório de erros, indicando a posição exata do erro no texto de entrada.
    * Adicionar suporte para operadores unários (ex: `-5` ou `+10`).