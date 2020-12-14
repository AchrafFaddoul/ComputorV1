# ComputorV1
ComputorV1 is a program that solves a polynomial of second or lower degree equation, and capable of showing at least:

The equation in its reduced form.
The degree of the equation.
It’s solution(s) and the polarity of the discriminant if it makes sens

## Usage:
python3 -m pip install -r requirements.txt

### solve equation:
python3 computor.py "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"

### solve equation and plot result
python3 plot.py "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1" -v

### Python version
Python 3.7.9
