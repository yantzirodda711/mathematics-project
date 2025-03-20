import math
def calculate_pi(n):
    """Uses the Bailey-Borwein-Plouffe algorithm to estimate pi"""
    x = 4*math.sqrt(2)
    y = 2**(-1-n*math.log2(x)/2/n)
    s = math.sqrt(x+y)-math.sqrt(x-y)
    return s*s/8
print(calculate_pi(10))