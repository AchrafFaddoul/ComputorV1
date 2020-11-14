import sys

def is_equation(expression):
    for c in expression:
        if (c.isalpha() or c.isdigit() 
            or c == '=' or c == '+' or c == '-' 
                or c == '*' or c == '^' or c == '.'):
            continue
        else:
            return False
    return True


def scanner(expression):
    return is_equation(expression)

def split_polynomial(equation):
    expressions = equation.replace(" ", "").split(sep='=')
    if len(expressions) != 2:
        return False
    return expressions


def get_input():
    if len(sys.argv) != 2:
        exit("bad input")
    return sys.argv[1];

def tokenizer(expressions):
    print(expressions)
    left_exp = []
    right_exp = []
    equation = {'left_expr': left_exp, 'right_expr': right_exp}
    elm = {'coeff': 0, 'exp': 0}
    print(elm['coeff'], "hello world")

def parser():
    equation = get_input()
    expressions = split_polynomial(equation)
    if not expressions:
        exit("this expression are not an equation")
    if not scanner(expressions[0]):
        exit("this expression are not an equation")
    if not scanner(expressions[1]):
        exit("this expression are not an equation")
    tokenizer(expressions)
    print("done")
