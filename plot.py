import computor
import sys
import numpy as np
import matplotlib.pyplot as plt


def get_input_plot():
    if len(sys.argv) != 3 or sys.argv[2] != '-v':
        exit("bad input")
    return sys.argv[1]


def plot_quadratic_pol():
    True
