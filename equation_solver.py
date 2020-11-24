def deg_extractor(equation):
    if not len(equation):
        return 0
    return equation[0]['expo']


def coeff_modifier(coeff, deg, min_deg):
    string = ''
    if coeff < 0:
        coeff *= -1
        string = '- ' if deg != min_deg else '-'
    else:
        string = '+ ' if deg != min_deg else ''
    try:
        string += str(int(coeff)) if not coeff % 1 else str(coeff)
    except:
        exit('bad input')
    string += ' '
    return string


def exponent_modifier(expo):
    string = '* X^'
    string += str(expo) + ' '
    return string


def reduced_form_generator(equation):
    reduced_polynomial = ''
    equation_rev = [elm for elm in reversed(equation)]
    min_deg = equation_rev[0]['expo']
    for elm in equation_rev:
        reduced_polynomial += coeff_modifier(
            elm['coeff'], elm['expo'], min_deg)
        reduced_polynomial += exponent_modifier(elm['expo'])
    reduced_polynomial += '= 0'
    reduced_polynomial = 'Reduced form: ' + reduced_polynomial
    return reduced_polynomial


def discriminant_calculator(equation):
    print(equation)
    True


def linear_polynomial_solver(equation):
    print(equation)
    True


def equation_solver(equation):
    deg = deg_extractor(equation)
    if deg == 0:
        null_deg_msg = 'Polynomial degree: 0'
        msg = 'all real numbers are a solution' if (
            not len(equation) or equation[0]['coeff'] == 0) else 'equation unsolvable'
        exit('{}\n{}'.format(null_deg_msg, msg))
    reduced_polynomial = reduced_form_generator(equation)
    print(reduced_polynomial)
    print('Polynomial degree: {}'.format(deg))
    if equation[-1]['expo'] < 1:
        exit('The polynomial degree is stricly smaller than 0, I can\'t solve it')
    elif equation[0]['expo'] > 2:
        exit('The polynomial degree is stricly greater than 2, I can\'t solve it')
    if deg == 1:
        linear_polynomial_solver(equation)
        True

    # discriminant_calculator(equation)
