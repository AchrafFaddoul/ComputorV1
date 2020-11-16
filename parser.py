import sys

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
    return sys.argv[1];

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

def coeff_expo_parser(exprs):
    equation = [[],[]]
    i = 0
    for expr in exprs:
        for token in expr:
            lst = token.split(sep='*')
            equation[i].append({
                'coeff': lst[0],
                'expo': lst[1]
            })
        i = i + 1
            
    return equation

# if sub-string in string[-3 -1]
def parser():
    tokens = []
    equation = get_input()
    expressions = split_polynomial(equation)
    if not expressions:
        exit("this expression are not an equation")
    if not scanner(expressions):
        exit("this expression are not an equation")
    exprs = tokenizer(expressions)
    equation = coeff_expo_parser(exprs)
    print(equation[0], '\n', equation[1])
    print("done")
