"""

The objective of this project is to create a simple calculator that can evaluate expressions like 1 + 2 * 3 or (1 + 2) * 3.
The particularity is that the calculator evaluates the expression from a string. 
It uses a lexer to evaluate the expression and tokenize it (Lexer class).
It then uses a parser to parse the tokens and create an abstract syntax tree (Parser class).
And finally, it uses an interpreter to evaluate the abstract syntax tree (Interpreter class).
Cheers,

"""


PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MUL'
DIVIDE = 'DIV'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
INTEGER = 'INTEGER'
FLOAT = 'FLOAT'
DIGITS = '0123456789'


class NumberNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return str(self.token.value)


class BinaryOperation:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    
    def __repr__(self):
        return '({}, {}, {})'.format(self.left, self.operator, self.right)


class UnaryOperation:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def __repr__(self):
        return '({} {})'.format(self.operator, self.right)


class Token:
    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type

    def __repr__(self):
        if self.type not in [INTEGER, FLOAT]:
            return f'{self.type}'
        return f'{self.type}:{self.value}'
    

class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.current_index = -1
        self.tokens = []
        self.advance()

    def advance(self):
        self.current_index += 1
        if self.current_index >= len(self.expression):
            self.current_char = None
        else:
            self.current_char = self.expression[self.current_index]
    
    def get_tokens(self):
        while self.current_char is not None:
            if self.current_char in DIGITS:
                num = ''
                while self.current_char is not None and self.current_char in DIGITS or self.current_char == '.':
                    num += self.current_char
                    self.advance()
                if '.' in num:
                    self.tokens.append(Token(float(num), FLOAT))
                else:
                    self.tokens.append(Token(int(num), INTEGER))
            elif self.current_char == ' ':
                self.advance()
            elif self.current_char == '+':
                self.tokens.append(Token(self.current_char, PLUS))
                self.advance()
            elif self.current_char == '-':
                self.tokens.append(Token(self.current_char, MINUS))
                self.advance()
            elif self.current_char == '*':
                self.tokens.append(Token(self.current_char, MULTIPLY))
                self.advance()
            elif self.current_char == '/':
                self.tokens.append(Token(self.current_char, DIVIDE))
                self.advance()
            elif self.current_char == '(':
                self.tokens.append(Token(self.current_char, LPAREN))
                self.advance()
            elif self.current_char == ')':
                self.tokens.append(Token(self.current_char, RPAREN))
                self.advance()

        return self.tokens
    

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.token_index = -1
        self.advance()
    
    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]

    def parse(self):
        return self.expr()
    
    def factor(self):
        token = self.current_token
        if token.type in (PLUS, MINUS):
            self.advance()
            factor = self.factor()
            return UnaryOperation(token, factor)
        
        elif token.type in (INTEGER, FLOAT):
            self.advance()
            return NumberNode(token)
        
        elif token.type == LPAREN:
            self.advance()
            expr = self.expr()
            if self.current_token.type == RPAREN:
                self.advance()
                return expr
            else:
                return None
        else:
            return None

    def expr(self):
        return self.bi_op(self.term, (PLUS, MINUS))

    def term(self):
        return self.bi_op(self.factor, (MULTIPLY, DIVIDE))

    def bi_op(self, func, operations):
        left = func()
        while self.current_token.type in operations:
            op = self.current_token
            self.advance()
            right = func()
            left = BinaryOperation(left, op, right)

        return left
    

class Number:
    def __init__(self, value):
        self.value = value
    
    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
    
    def subtracted_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
    
    def multiplied_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
    
    def divided_by(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)
    
    def __repr__(self) -> str:
        return str(self.value)
    

class Interpreter:
    
    def visit(self, node):
        name = node.__class__.__name__
        if name == 'NumberNode':
            return self.visit_NumberNode(node)
        elif name == 'BinaryOperation':
            return self.visit_BinaryOperation(node)
        elif name == 'UnaryOperation':
            return self.visit_UnaryOperation(node)
        else:
            raise Exception(f'Unknown node: {name}')

    def visit_NumberNode(self, node):
        return Number(node.token.value)
    
    def visit_UnaryOperation(self, node):
        if node.operator.type == PLUS:
            return self.visit(node.right)
        elif node.operator.type == MINUS:
            return self.visit(node.right).multiplied_by(Number(-1))
        else:
            raise Exception(f'Unknown operator {node.operator.type}')
    
    def visit_BinaryOperation(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.operator.type == PLUS:
            return left.added_to(right)
        elif node.operator.type == MINUS:
            return left.subtracted_by(right)
        elif node.operator.type == MULTIPLY:
            return left.multiplied_by(right)
        elif node.operator.type == DIVIDE:
            return left.divided_by(right)
        else:
            raise Exception(f'Unknown operator {node.operator.type}')


def calc(expression):
    lexer = Lexer(expression)
    result = lexer.get_tokens()

    parser = Parser(result)
    result = parser.parse()

    interpreter = Interpreter()
    result = interpreter.visit(result)
    return result.value
