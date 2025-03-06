import random

def generate_random_code(length=10):
    """Generates a random string of letters and digits"""
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    code = ''
    for i in range(length):
        if i % 2 == 0:
            code += random.choice(letters)
        else:
            code += random.choice(numbers)
    return code
