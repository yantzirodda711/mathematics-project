import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(num_samples):
    """
    Generate a random dataset of shape (num_samples, 2).

    Parameters:
    - num_samples: Number of samples to generate.

    Returns:
    - x: A randomly generated dataset of shape (num_samples, 2).
    - y: The corresponding target values for the dataset.
    """

    # Generating random data
    np.random.seed(0)
    x = np.random.rand(num_samples, 1) * 5  # X-axis values
    y = 2 * x + np.random.randn(num_samples) * 3

    return x, y

def plot_data(x, y):
    """
    Plot the data in a scatter plot.

    Parameters:
    - x: The dataset for the X-axis.
    - y: The dataset for the Y-axis.
    """

    plt.scatter(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Random Data Scatter Plot')
    plt.show()

if __name__ == "__main__":
    x, y = generate_random_data(100)  # Generate random data for demonstration
    plot_data(x, y)
