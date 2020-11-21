def deg_extractor(equation):
    return equation[0]['expo']

def coeff_modifier(coeff, deg):
    string = ''
    if coeff < 0:
        coeff *= -1
        if deg != 0:
            string = '- '
        else:
            string = '-'
    else:
        if deg != 0:
            string = '+ '
        else:
            string = '+'
    string += str(int(coeff)) if coeff % 10 else str(coeff)
    string += ' '
    return string


def reduced_form_generator(equation):
    reduced_polynomial = ''
    equation_rev = [elm for elm in reversed(equation)]
    for elm in equation_rev:
        reduced_polynomial += coeff_modifier(elm['coeff'], elm['expo'])
    print(reduced_polynomial)
        

def equation_solver(equation):
    deg = deg_extractor(equation)
    print(equation)
    reduced_form_generator(equation)