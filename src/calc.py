
def multiply(a, b):
    return a * b


def sum_local(*args):
    return sum(args)


def division(a, b):
    return a / b


def subtraction(a, b):
    return a - b


mapping = {"*": multiply, "+": sum_local, "/": division, "-": subtraction}


