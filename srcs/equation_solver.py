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
    except BaseException:
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
    delta_coeffs = [0, 0, 0]
    i = 0
    for elm in equation:
        delta_coeffs[i] = elm['coeff']
        i += 1
    delta = delta_coeffs[1] * delta_coeffs[1] - \
        (4 * delta_coeffs[0] * delta_coeffs[2])
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
        sol_msg += str(round(sol, 6))
    elif equa_len == 1:
        sol_msg += '0'
    print(sol_msg)
    return True


def complex_solution_formator(delta_sqrt, re, im):
    sign1 = ' + ' if (im > 0) else ' - '
    sign2 = ' - ' if (im > 0) else ' + '
    if im < 0:
        im *= -1
    x1 = f"{str(round(re, 6))}{sign1}{str(round(im, 6))}i"
    x2 = f"{str(round(re, 6))}{sign2}{str(round(im, 6))}i"
    solution = {'delta': -1, 'x1': x1, 'x2': x2}
    return solution


def quadratic_polynomial_solver(solution_data):
    if solution_data['delta'] > 0:
        delta_sqrt = solution_data['delta'] ** 0.5
        x1 = (- solution_data['b'] + delta_sqrt) / (2 * solution_data['a'])
        x2 = (- solution_data['b'] - delta_sqrt) / (2 * solution_data['a'])
        solution = {'delta': 1, 'x1': str(
            round(x1, 6)), 'x2': str(round(x2, 6))}
        solution = 'Discriminant is strictly positive, the two solutions are:\n{}\n{}'.format(
            solution['x1'], solution['x2'])
        return solution
    elif not solution_data['delta']:
        x = (- solution_data['b']) / (2 * solution_data['a'])
        solution = {'delta': 0, 'x': str(x)}
        solution = 'Discriminant equal zero, the only solution is:\n{}'.format(
            solution['x'])
        return solution
    else:
        delta_sqrt = (-1 * solution_data['delta']) ** 0.5
        re = - solution_data['b'] / (2 * solution_data['a'])
        im = delta_sqrt / (2 * solution_data['a'])
        solution = complex_solution_formator(delta_sqrt, re, im)
        solution = 'Discriminant is strictly negative, the two solutions are:\n{}\n{}'.format(
            solution['x1'], solution['x2'])
    return solution


def equation_solver(equation):
    deg = deg_extractor(equation)
    if deg == 0:
        null_deg_msg = 'Polynomial degree: 0'
        msg = 'all real numbers are a solution' if (not len(
            equation) or equation[0]['coeff'] == 0) else 'there is no solution for this equation'
        exit('{}\n{}'.format(null_deg_msg, msg))
    reduced_polynomial = reduced_form_generator(equation)
    print(reduced_polynomial)
    print('Polynomial degree: {}'.format(deg))
    if equation[-1]['expo'] < 0:
        exit('The polynomial degree is stricly smaller than 0, I can\'t solve it')
    elif equation[0]['expo'] > 2:
        exit('The polynomial degree is stricly greater than 2, I can\'t solve it')
    if deg == 1:
        if not linear_polynomial_solver(equation):
            exit('something went wrong during solution calculation')
        return (equation)
    solution_data = discriminant_calculator(equation)
    solution = quadratic_polynomial_solver(solution_data)
    print(solution)
    return equation
