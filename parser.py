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
                tokens.append(expression[j:i])
                j = i
        tokens.append(expression[j:i+1])
        equation.append(tokens)
    return equation

def coeff_expo_parser(expressions):
    exprs = tokenizer(expressions)
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
    #to write in an other clean way
    except:
        exit('coefficient not properly formated')
    return coeff

def is_exponent(expo):
    exponents = ['X^0', 'X^1', 'X^2']
    if not expo in exponents:
        exit('exponent not properly formated')
    expo = int(expo[-1:])
    return expo

def semantic_analyser(equation):
    for expression in equation:
        for elm in expression:
            elm['coeff'] = is_coeff(elm['coeff'])
            elm['expo'] = is_exponent(elm['expo'])

def equation_simplifier(equation):
    i = 0
    for elm in equation[1]:
        elm['coeff'] = elm['coeff'] * -1
        equation[0].append(elm)
        if len(equation[1]) > 0:
            equation[1].pop(i)
        i += 1
    equation[0] = sorted(equation[0], key=lambda k: k['expo'], reverse=True)
    for i in equation[0]:
        for j in equation[0]:
            if j['expo'] == i['expo'] and equation[0].index(i) != equation[0].index(j):
                i['coeff'] += j['coeff']
                if len(equation[0]) > 0:
                    equation[0].pop(equation[0].index(j))
    coeff_lst = [elm['coeff'] for elm in equation[0]]
    gcd = find_gcd(coeff_lst)
    if (gcd > 1):
        for elm in equation[0]:
            elm['coeff'] = elm['coeff'] / gcd

def parser():
    equation = get_input()
    expressions = split_polynomial(equation)
    if not expressions:
        exit("this expression isn't an equation")
    if not scanner(expressions):
        exit("this expression isn't an equation")
    equation = coeff_expo_parser(expressions)
    if not equation:
        exit("this expression isn't an equation")
    semantic_analyser(equation)
    equation_simplifier(equation)
    print(equation)
    print("done")
