import numpy as np
from scipy.integrate import odeint

def f(x):
    return x ** 2 - 4 * x + 3

initial_guess = [0.5]
solution = odeint(f, initial_guess, 10)
print(solution)
