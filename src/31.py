def fibonacci(n):
    """
    Generate a list containing the Fibonacci sequence up to the nth number.
    
    Parameters:
    n (int): The length of the Fibonacci sequence to generate.
    
    Returns:
    list: A list containing the Fibonacci sequence up to the nth number.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence

# Example usage
n = 10
print(fibonacci(n))
