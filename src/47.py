import math

def calculate_factorial(n):
    """
    Calculate the factorial of a given number n.
    
    Parameters:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Example usage
print(calculate_factorial(5))  # Output: 120
