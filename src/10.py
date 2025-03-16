def calculate_pi(precision=16):
    # Math.PI is a mathematical constant approximately equal to 3.141592653589793
    # Calculate pi using the Bailey-Borwein-Plouffe algorithm
    x = 0
    y = 1
    result = 0
    for i in range(precision):
        if (i % 2 == 0):
            x = x * (i * 2 + 1) * 4
            y = y * (i * 2 + 1) * 4 - 1
            result += x / y
    return round(result, precision)
