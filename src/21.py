import numpy as np

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return 3.14 * radius ** 2

# Example usage
radius = 5
area = calculate_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")
