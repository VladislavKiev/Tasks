# Four real numbers are given: x1, y1, x2, y2. calculate the distance between point (x1, y1) and (x2, y2). Consider four real numbers and print the result of this function.

x1 = int(input('Enter value x1 >>> '))
x2 = int(input('Enter value x2 >>> '))
y1 = int(input('Enter value y1 >>> '))
y2 = int(input('Enter value y2 >>> '))

res = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) ** (0.5)

print(res)
