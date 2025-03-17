
import numpy as np

def calculate_pi(n):
    """Use the Monte Carlo method to estimate pi"""
    inside = 0
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n