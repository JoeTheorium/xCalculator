from sympy import symbols, simplify, sqrt, factorial

# Functions for basic mathematical operations

def add(a, b):
    x, y = symbols('x y')  # Define symbolic variables "x" and "y"
    expression = x + y  # Create an addition expression
    result = expression.subs({x: a, y: b})  # Substitute values "a" and "b" into the expression
    return result


def subtract(a, b):
    x, y = symbols('x y')
    expression = x - y
    result = expression.subs({x: a, y: b})
    return result


def multiply(a, b):
    x, y = symbols('x y')
    expression = x * y
    result = expression.subs({x: a, y: b})
    return result


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    x, y = symbols('x y')
    expression = x / y
    result = expression.subs({x: a, y: b})
    return result


def raise_to_power(base, exponent):
    x, y = symbols('x y')
    expression = x ** y
    result = expression.subs({x: base, y: exponent})
    return result


def calculate_square_root(a):
    x = symbols('x')
    expression = sqrt(x)
    result = expression.subs({x: a})
    return result


def calculate_factorial(a):
    x = symbols('x')
    expression = factorial(x)
    result = expression.subs({x: a})
    return result
