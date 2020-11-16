import sys

def is_equation(expressions):
    for expression in expressions:
        print(expression)
        for c in expression:
            if (c.isalpha() or c.isdigit() 
                or c == '=' or c == '+' or c == '-' 
                    or c == '*' or c == '^' or c == '.'):
                continue
            else:
                return False
    return True

def scanner(expressions):
    return is_equation(expressions)

def split_polynomial(equation):
    expressions = equation.replace(" ", "").split(sep='=')
    if len(expressions) != 2 or  len(expressions[0]) == 0 or len(expressions[1]) == 0:
        return False
    return expressions


def get_input():
    if len(sys.argv) != 2:
        exit("bad input")
    return sys.argv[1];

def tokenizer(expression):
    tokens = []
    j = 0
    for i in range(0, len(expression)):
        if expression[i] == '+' or expression[i] == '-':
            tokens.append(expression[j:i])
            j = i + 1
    tokens.append(expression[j:i+1])
    return tokens

def parser():
    tokens = []
    equation = get_input()
    expressions = split_polynomial(equation)
    if not expressions:
        exit("this expression are not an equation")
    if not scanner(expressions):
        exit("this expression are not an equation")
    tokens.append(tokenizer(expressions[0]))
    tokens.append(tokenizer(expressions[1]))
    print(tokens)
    print("done")
