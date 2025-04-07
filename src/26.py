import numpy as np
from scipy.optimize import minimize
from math import log

def calculate_derivative(func, x):
    if len(x) != 1 or not callable(func):
        raise ValueError("x should be a list of values and func should be a function")
    return [func(i) for i in x]

def square_root_of_x(x, y=0.5):
    return np.sqrt(x - y)

def sum_square(x, n):
    if len(x) != 1 or not callable(sum_square):
        raise ValueError("x should be a list of values and sum_square should be a function")
    return (sum_square(i) for i in x)

# Example usage:
numbers = [0.5, -2, 3]
derivative = calculate_derivative(square_root_of_x, numbers)
y_values = np.arange(-10, 10.1, 0.1)
result = minimize(sum_square, y_values, method='nelder-mead', options={'disp': True})
print(result)

# Example usage:
values = [1, 2]
derivative = calculate_derivative(square_root_of_x, values)
y_values = np.arange(-5, 6.1, 0.1)
result = minimize(sum_square, y_values, method='nelder-mead', options={'disp': True})
print(result)
