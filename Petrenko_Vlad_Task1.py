# 1. Two integers are given. Output the value of the smallest of them.

a = int(5)
b = int(4)
if a > b:
    print('"b" less and value is >>>', b)
elif a == b:
    print('values are equal')
else:
    print('"a" less and value is >>>', a)

c = int(input('Enter value c >>> '))
d = int(input('Enter value d >>> '))
if c > d:
    print('"d" less and value is >>>', b)
elif c == d:
    print('values are equal')
else:
    print('"c" less and value is >>>', a)

# 2. Two squares of a chessboard are given. If they are colored in the same color, then print the word YES, and if they are in different colors - then NO. The program receives as input four numbers from 1 to 8 each, specifying the column number and line number, first for the first cell, then for the second cell.

a = int(input('Enter first row>>>> '))
b = int(input('Enter first column>>>> '))
c = int(input('Enter second row>>>> '))
d = int(input('Enter second column>>>> '))
e = int(a * b % 2 == 0)
f = int(c * d % 2 == 0)
if min(a, b, c, d) > 0 and max(a, b, c, d) <= 8:
    if e == 0:
        print('the first color is black')
    else:
        print('the first color is white')
    if f == 0:
        print('the second color is black')
    else:
        print('the second color is white')
    if e == f:
        print('Yes')
    else:
        print('No')
else:
    print('Enter correct value')

# 3. If a temperature is entered in degrees Celsius, it is converted to a temperature in Fahrenheit. Or vice versa: Fahrenheit temperature is converted to Celsius temperature.

a = input('Enter the temperature, the last character should be C or F >>> ')
temp = float(a[:-1])
if a[-1] == 'F':
    c = (temp - 32) * 5/9
    print(c, 'C')
elif a[-1] == 'C':
    f = temp * 9/5 + 32
    print(f, 'F')
else:
    print('Enter correct value')

# 4. From a list of random numbers, identify and display the odd numbers.
from random import randint

lst_1 = [randint(0, 12) for i in range(8)]
print(lst_1)
for x in lst_1:
    if x % 2 != 0:
        print('odd value', x)

# 5. An integer is entered to indicate the ASCII character code. Determine if this is an English letter code or some other symbol.

v = int(input('Enter code in DEC >>> '))
if 65 <= v <= 90 or 97 <= v <= 122:
    print('Latin letters of different registers')
else:
    print('other')

# 6. Two integers are entered. Check if the first is divisible by the second. Display a message about this, as well as the remainder (if any) and private (in any case).

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

# 7. 5 digits are entered alternately, display their sum (using for)

res = 0
for i in range(5):
    x = int(input('Enter value>>> '))
    res += x
print(res)

# 8. You are given two integers A and B. Print all numbers from A to B, inclusive, in ascending order if A <B, or in descending order otherwise.

a = int(input('Enter value A >>> '))
b = int(input('Enter value B >>> '))

if a > b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    for i in range(a, b + 1):
        print(i)

# 9. With a for loop, display a rhombus

n = 10
m = 1
for i in range(n):
    print(n * "*" + "A" * m + n * "*")
    m += 2
    n -= 1
    print('A' * (i * 2 + 3))
    # print(n)
    n = 10
    m = 1
for i in range(n):
    print(m * "*" + "A" * (2 * n - 1) + m * "*")
    n -= 1
    m += 1


# 10. Calculate the sum of a number series from 0 to 14 inclusive. For example, 0 + 1 + 2 + 3 +… + 14;

res = 0
for i in range(15):
    res += i
print(res)

# 11. Multiply all even values in the range 0 to 436

a = 1
b = 436
for i in range(a, b):
    if i % 2 == 0:
        a = a*i
print(a)

# 12. A random real number is given. Determine the maximum digit of this number. Execution example: 56.457 -> 7

v = float(input('Input value >>> '))
vmax = 0
while v % 10 != 0:
    v = v*10
    # v = int(v)
    print(v)
v = int(v)
c = str(v)
for i in c:
    i = int(i)
    if i > vmax:
        vmax = i
print('max is', vmax)

# 13. The factorial of the number n is the number 𝑛! = 1 ∙ 2 ∙ 3∙… ∙ 𝑛. Create a program that calculates the factorial of a user-entered number. (Cycle!)

a = int(input('Enter value >>> '))
res = 1
for i in range(1, a+1):
    res = i * res
    print(res)
print(res)

# 14. Using nested loops and the functions print (‘*’, end = ’’), print (‘’, end = ’’) and print () print the right triangle.

a = int(input('enter the length of the leg'))

for i in range(a + 1):
    print('* ' * i)
for i in range(a + 1):
    print(' ' * (2 * a) + i * ' *')
    a -= 1

# 15. The user makes a deposit in the amount of N $ for a period of years at 11.5% per annum (each year the size of his deposit increases by 11.5%. This money is added to the amount of the deposit, and next year there will also be interest on them). Write a program where the user enters the arguments a and years, and calculate the amount that will be on the user's account after years.

am = float(input('Enter amount >>>'))
years = int(input('Enter the term in years>>> '))
dep = 0.115
for i in range(1, years + 1):
    am = am + am*dep
print('The result would be ', am)

# 16. The user enters the year. Determine whether it is high-axle or not.

year = int(input('Enter year'))
if year % 4 == 0:
    print('High-axel')
else:
    print('None')

# 17. Write a program that asks for three integers a, b, and x and prints True if x is between a and b, or False otherwise.

a = int(input('Enter value a >>> '))
b = int(input('Enter value b >>> '))
x = int(input('Enter value x >>> '))

if a < x < b:
    print('True')
else:
    print('False')

# 18 Four real numbers are given: x1, y1, x2, y2. calculate the distance between point (x1, y1) and (x2, y2). Consider four real numbers and print the result of this function.

x1 = int(input('Enter value x1 >>> '))
x2 = int(input('Enter value x2 >>> '))
y1 = int(input('Enter value y1 >>> '))
y2 = int(input('Enter value y2 >>> '))

res = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) ** (0.5)

print(res)
