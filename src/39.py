import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(x, a, b):
    """
    Define a simple sinusoidal function.
    
    Parameters:
        x (float): The input value for the function.
        a (float): Coefficient of the sine term.
        b (float): Amplitude of the sine wave.
        
    Returns:
        float: The value of the function at x.
    """
    return a * np.sin(b * x)

def fit_sine(x, y):
    """
    Fit a simple sinusoidal curve to a given set of data points using curve_fit.
    
    Parameters:
        x (float): Coordinates for the sine values.
        y (list): List of y-values corresponding to each x-coordinate.
        
    Returns:
        tuple: Coefficients [a, b] of the fitted curve.
    """
    params, _ = curve_fit(f, x, y)
    return params

# Example usage
x_data = np.linspace(0, 2 * np.pi, 100)
y_data = f(x_data, 5, 3)  # Simple sinusoidal function with a coefficient of 5 and amplitude 3

a_fit, b_fit = fit_sine(x_data, y_data)

print(f"Fitted parameters: {a_fit:.2f}, {b_fit:.2f}")
