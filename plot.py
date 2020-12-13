from parser import split_polynomial, scanner, coeff_expo_parser, semantic_analyser
from equation_simpilifier import equation_simplifier
from equation_solver import equation_solver
import sys
import numpy as np
import matplotlib.pyplot as plt


def get_input_plot():
    if len(sys.argv) != 3 or sys.argv[2] != '-v':
        exit("bad input")
    return sys.argv[1]


def plot_parser():
    equation = get_input_plot()
    expressions = split_polynomial(equation)
    if not expressions or not scanner(expressions):
        exit("this expression isn't an equation")
    equation = coeff_expo_parser(expressions)
    if not equation:
        exit("this expression isn't an equation")
    semantic_analyser(equation)
    return equation


def plot_quadratic_pol(equation):
    x = np.linspace(-50, 50, 1000)
    y = ''
    for elm in equation:
        if elm['coeff'] >= 0:
            y += '+'
        y += '{}*x**{}'.format(elm['coeff'], elm['expo'])
    y = eval(y)
    ax = plt.subplot()
    ax.plot(x, y)
    plt.show()


def main():
    equation = plot_parser()
    equation = equation_simplifier(equation)
    equation = equation_solver(equation)
    if not equation:
        exit('this equation isn\t a quadratic polynomial')
    plot_quadratic_pol(equation)


if __name__ == "__main__":
    main()
