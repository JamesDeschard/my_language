# Evaluating a mathematical expression
The objective of this project is to create a simple calculator that can evaluate expressions like 1 + 2 * 3 or (1 + 2) * 3. The particularity is that the calculator evaluates the expression from a string.  It uses a lexer to evaluate the expression and tokenize it (Lexer class). It then uses a parser to parse the tokens and create an abstract syntax tree (Parser class).It finally uses an interpreter to evaluate the abstract syntax tree (Interpreter class). Cheers,

## Numbers
Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

## Operators
Supported mathematical operators:

- Multiplication *
- Division / (as floating point division)
- Addition +
- Subtraction -
-Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

## Parentheses
Supports multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

## Whitespace
There may or may not be whitespace between numbers and operators.
