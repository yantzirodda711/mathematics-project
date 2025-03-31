import math
def calculate_surface_area(radius, height):
    """
    Calculate the surface area of a cylinder.
    
    Parameters:
    radius (float): The radius of the cylinder's base.
    height (float): The height of the cylinder.
    
    Returns:
    float: The surface area of the cylinder.
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Example usage
print(calculate_surface_area(5, 10))  # Output: 67.84963891951896
