import numpy as np
from sympy import symbols, solve

x = symbols('x')
equation = 3*x**2 - x + 1 # Example quadratic equation

solution = solve(equation, x)
print(solution)
