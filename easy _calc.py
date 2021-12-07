def add(a, b):
    return a + b


def div(a, b):
    return a / b


def mult(a, b):
    return a * b


def sub(a, b):
    return a - b


calc_ = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}
try:
    first = float(input('Enter first numb >>> '))
    operation = input('Enter operation ({}) >>> '.format(' '.join(calc_.keys())))
    second = float(input('Enter second numb >>> '))
    print(calc_[operation](first, second))
except ValueError as e:
    print('Incorrect Values,', e)
except ZeroDivisionError as e:
    print('Zero division or infinity,', e)
    import math
    print(math.inf)
except KeyError as e:
    print('Key error, invalid operation, ', e)
except Exception as e:
    print(e, type(e))
finally:
    print('Thanks for using calc')
