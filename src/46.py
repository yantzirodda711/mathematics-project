import numpy as np
from scipy.integrate import odeint

def simple_differential_equation(y, t, f1, f2):
    """
    A simple differential equation model.
    Parameters:
        y: list or numpy array of dependent variables.
        t: time vector.
        f1: coefficient for the first derivative (f1).
        f2: coefficient for the second derivative (f2).

    Returns:
        float: The value of the function at t.
    """
    # Define the ODE
    y_prime = [f1 * y[0] + 3.5, -f2 * y[0]]
    
    return np.array(y_prime)

# Example values
y0 = [0, 0]
t = np.linspace(0, 10, 100)  # Time points

# Solve the ODE
sol = odeint(simple_differential_equation, y0, t)
