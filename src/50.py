import numpy as np
from scipy.optimize import minimize

def f(x):
    y = 2 * x[0] - x[1]
    g = (x[0]**2 + x[1]**2)**0.5
    return y, g

initial_guess = [0.5, 0.3]

result = minimize(f, initial_guess)
print(result.x)

# Example of using the result to solve a problem
def cost_function(x):
    y, g = f(x)
    return (1 - x[0])**2 + 4 * (x[1] - y)**2

initial_guess_2 = [1.5, 0.7]
result_2 = minimize(cost_function, initial_guess_2, method="lbfgs")
print(result_2.x)
