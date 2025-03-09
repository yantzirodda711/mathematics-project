import random
def get_random_mathematical_expression(variables):
    """
    Generate a random mathematical expression using the given variables.
    """
    operators = ["+", "-", "*", "/"]
    operands = []
    for variable in variables:
        operands.append(str(variable))
    while len(operands) < 3:
        operands.append(str(random.randint(1, 10)))
    expression = " ".join(operands)
    return expression
