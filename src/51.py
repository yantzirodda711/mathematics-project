def square_root(n):
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    elif n == 0 or n == 1:
        return n

    # Perform binary search to find the integer part of the square root
    start = 0
    end = n + 1
    result = (end - start) / 2.0

    while abs(result**2 - n) > 1e-6: 
        if result**2 < n:
            start = result
        else:
            end = result
        result = (end - start) / 2.0

    return round(result, 5)
