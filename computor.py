from parser import parser
from equation_simpilifier import equation_simplifier
from equation_solver import equation_solver, deg_extractor


def main():

    equation = parser()
    equation = equation_simplifier(equation)
    equation_solver(equation)


if __name__ == "__main__":
    main()
