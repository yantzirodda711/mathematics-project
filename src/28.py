import numpy as np

def calculate_sine_values(num_samples=100):
    """
    Generate an array of sine values at specific intervals.
    
    Args:
    - num_samples (int): The number of samples to generate.

    Returns:
    - numpy.ndarray: An array containing the sine values of each interval from 0 to pi/2.
    """
    angle_increment = np.linspace(0, np.pi / 2, num_samples)
    sine_values = np.sin(angle_increment)
    return sine_values

# Generate the sine values
sine_values = calculate_sine_values()
print(sine_values)

# Visualize the first few elements of the array for a visual reference.
import matplotlib.pyplot as plt
plt.plot(sine_values)
plt.show()
