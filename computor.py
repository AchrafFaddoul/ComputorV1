from parser import parser
from equation_simpilifier import equation_simplifier

def main():
    
    equation = parser()
    equation = equation_simplifier(equation)
    print(equation)

if __name__ == "__main__":
    main()