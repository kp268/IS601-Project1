import math
from CsvReader import CsvReader


def division(a, b):
    a = int(a)
    b = int(b)
    c = b / a
    return round(c, 9)


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def squarefunc(a):
    a = int(a)
    a = a ** 2
    return a


def squarerootfunc(a):
    return round((int(a)**.5), 8)


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = squarefunc(a)
        return self.result

    def squareroot(self, a):
        self.result = squarerootfunc(a)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result


