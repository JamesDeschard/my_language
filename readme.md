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

## The Lexer

A lexer is a software program that performs lexical analysis. Lexical analysis is the process of separating a stream of characters into different words, which in computer science we call 'tokens'.
Let's image you wish to run the following string in our script.py file: ``'(1 + 2) * 3'``.
The lexer will iterate through the string and create a list of tokens.

```python

 lexerised_result = [LPAREN, INTEGER:1, PLUS, INTEGER:2, RPAREN, MUL, INTEGER:3]

``` 

## The Parser

A parser goes one level further than the lexer and takes the tokens produced by the lexer and tries to determine if proper sentences have been formed. Parsers work at the grammatical level, lexers work at the word level.
In our example the parser would return the following.

```python
parsed_result = ((1, PLUS, 2), MUL, 3)
``` 

## The Interpreter

An interpreter is a kind of program that executes other programs. When you write Python programs , it converts source code written by the developer into intermediate language which is again translated into the native language / machine language that is executed. In our example, the Interpreter class will convert the Parser's return value into our desired result.

```python
 print(calc('(1 + 2) * 3'))
 
 #returns 9
``` 
