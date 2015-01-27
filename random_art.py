import random
from math import sin, cos, pi

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.
# Fav piece: seed = 400752294477970573


class Express:
    def __init__(self):
        self.location = []

    def __str__(self):
        return str(self.location)

    def random_value(self, x, y):
        value = 3
        for rule, location in self.location:
            if rule == 'pow' and location == 'y':
                value = (pow(pi * y, random.randint(0, 2)) * sin(pi * y))
            elif rule == 'cos' and location == 'y':
                value *= cos(pi * x * y)
            elif rule == 'sin' and location == 'y':
                value *= (sin(pi * y) * sin(pi * x))
            elif rule == 'pow' and location == 'x':
                value = pow(pi * x, random.randint(0, 2))
            elif rule == 'cos' and location == 'x':
                value *= cos(pi * x)
            elif rule == 'sin' and location == 'x':
                value *= sin(pi * x)
        return value


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    # expr = lambda x, y: (random.random() * 2) - 1
    # return expr

    express = Express()
    choice_list = ['sin', 'cos', 'pow']

    for _ in range(random.randint(3, 10)):
        rule_int = random.random()

        if random.random() > .5:
            location = 'x'
        else:
            location = 'y'

        rule = random.choice(choice_list)

        express.location.append([rule, location])

    return express


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.random_value(x, y)
