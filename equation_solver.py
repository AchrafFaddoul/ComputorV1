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
    delta_coeffs = [0, 0, 0]
    i = 0
    for elm in equation:
        delta_coeffs[i] = elm['coeff']
        i += 1
    print(delta_coeffs)
    delta = delta_coeffs[1] ** 2 - (4 * delta_coeffs[0] * delta_coeffs[2])
    solution_data = {'a': delta_coeffs[0], 'b': delta_coeffs[1],
                     'c': delta_coeffs[2], 'delta': delta}
    return solution_data


def linear_polynomial_solver(equation):
    sol = 0
    equa_len = len(equation)
    if not equa_len or equa_len > 2:
        return (False)
    sol_msg = 'The solution is:\n'
    if equa_len == 2:
        sol = (equation[1]['coeff'] * -1) / equation[0]['coeff']
        sol_msg += str(sol)
    elif equa_len == 1:
        sol_msg += '0'
    print(sol_msg)
    return True


def quadratic_polynomial_solver(eq)


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
    if equation[-1]['expo'] < 0:
        print(equation[-1])
        exit('The polynomial degree is stricly smaller than 0, I can\'t solve it')
    elif equation[0]['expo'] > 2:
        exit('The polynomial degree is stricly greater than 2, I can\'t solve it')
    if deg == 1:
        if not linear_polynomial_solver(equation):
            exit('something went wrong during solution calculation')
        exit(0)
    discriminant_calculator(equation)
