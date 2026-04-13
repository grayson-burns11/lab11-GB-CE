"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return b/a
def logarithm(a, b):
    if a == 1 or b<=0 or a <=0:
        raise ValueError
    return math.log(a,b)
def exponent(a, b):
    return a**b

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Can't take square root of negative numbers")
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Inputs must be numbers")
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return b / a
def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Incorrect input for logarithm")
    return math.log(b, a)
def exp(a, b):
    return a ** b
