def add_numbers(a, b):
    """Add two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Subtract two numbers."""
    return a - b

def multiply_numbers(a, b):
    """Multiply two numbers."""
    return a * b

def divide_numbers(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    else:
        return a / b
