import sys
from tools import find_gcd

def is_equation(expressions):
    for expression in expressions:
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
    return sys.argv[1]

def tokenizer(expressions):
    equation = []
    for expression in expressions:
        tokens = []
        j = 0
        for i in range(0, len(expression)):
            if expression[i] == '+' or expression[i] == '-':
                if len(expression[j:i]):
                    tokens.append(expression[j:i])
                j = i
        tokens.append(expression[j:i+1])
        equation.append(tokens)
    return equation

def negative_exponent_handler(exprs):
    i = 0
    for expr in exprs:
        for j in range(0, len(expr)):
            if expr[j][0] == '-' and expr[j][1:].isdigit():
                if j > 0:
                    expr[j - 1] += expr[j]
        expr = [elm for elm in expr if not (elm[0] == '-' and elm[1:].isdigit())]
        exprs[i] = expr
        i += 1
    return exprs

def coeff_expo_parser(expressions):
    exprs = tokenizer(expressions)
    exprs = negative_exponent_handler(exprs)
    equation = [[],[]]
    i = 0
    for expr in exprs:
        for token in expr:
            lst = token.split(sep='*')
            if len(lst) != 2:
                return False
            equation[i].append({
                'coeff': lst[0],
                'expo': lst[1]
            })
        i = i + 1
    return equation

def is_coeff(coeff):
    try:
        coeff = float(coeff)
    except:
        exit('coefficient not properly formated')
    return coeff

def is_exponent(expo):
    unk = ['X^']
    if not expo[:2] in unk:
        exit('exponent not properly formated')
    expo = int(expo[2:])
    return expo

def semantic_analyser(equation):
    for expression in equation:
        for elm in expression:
            elm['coeff'] = is_coeff(elm['coeff'])
            elm['expo'] = is_exponent(elm['expo'])



def parser():
    equation = get_input()
    expressions = split_polynomial(equation)
    if not expressions:
        exit("this expression isn't an equation")
    if not scanner(expressions):
        exit("1 this expression isn't an equation")
    equation = coeff_expo_parser(expressions)
    if not equation:
        exit("2 this expression isn't an equation")
    semantic_analyser(equation)
    return equation
