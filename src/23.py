import numpy as np
from scipy import optimize

def f(x):
    """
    This is a simple function that we want to find the maximum of.
    """
    return x**2 - 4*x + 1

# We need an initial guess for the optimization
initial_guess = 0

result = optimize.minimize(f, initial_guess)
max_value = result.fun
print(max_value)
