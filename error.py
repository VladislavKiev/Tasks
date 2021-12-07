a = 5
b = int(input('>>> '))
if b == 0:
    raise ZeroDivisionError('looking in standard math')

print(a / b)

try:
    x = 2 / 2
except:
    import math
    print('Except!')
    x = math.inf
print(x)
