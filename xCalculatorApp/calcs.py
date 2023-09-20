from sympy import symbols, simplify, sqrt, factorial


def sumar(a, b):
    x, y = symbols('x y')
    expresion = x + y
    resultado = expresion.subs({x: a, y: b})
    return resultado


def restar(a, b):
    x, y = symbols('x y')
    expresion = x - y
    resultado = expresion.subs({x: a, y: b})
    return resultado


def multiplicar(a, b):
    x, y = symbols('x y')
    expresion = x * y
    resultado = expresion.subs({x: a, y: b})
    return resultado


def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    x, y = symbols('x y')
    expresion = x / y
    resultado = expresion.subs({x: a, y: b})
    return resultado


def elevar_potencia(base, exponente):
    x, y = symbols('x y')
    expresion = x ** y
    resultado = expresion.subs({x: base, y: exponente})
    return resultado


def calcular_raiz_cuadrada(a):
    x = symbols('x')
    expresion = sqrt(x)
    resultado = expresion.subs({x: a})
    return resultado


def calcular_factorial(a):
    x = symbols('x')
    expresion = factorial(x)
    resultado = expresion.subs({x: a})
    return resultado
