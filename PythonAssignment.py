import numpy as np
from scipy.optimize import minimize
def f(vars):
    x, y = vars
    return x**2 + y**2 + 3*x + 4*y + 5
initial_guess = [0, 0]  # Starting point (x=0, y=0)