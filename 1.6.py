# Two integers are entered. Check if the first is divisible by the second. Display a message about this, as well as the remainder (if any) and private (in any case).

x = int(input('Enter first value > '))
y = int(input('Enter second value > '))

if y == 0:
    print('division by zero is prohibited!')
else:
    print('the first number can be divisible by the second ')
    if x % y != 0:
        c = x % y
        print('remainder of the division ', c)
        print('quotient of division', x//y)
    else:
        print('quotient of division', x//y)




