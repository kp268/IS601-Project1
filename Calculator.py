

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def addition(a, b):
    c = a + b
    return c


def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

