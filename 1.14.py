# Using nested loops and the functions print (‘*’, end = ’’), print (‘’, end = ’’) and print () print the right triangle.

a = int(input('enter the length of the leg'))

for i in range(a + 1):
    print('* ' * i)
for i in range(a + 1):
    print(' ' * (2 * a) + i * ' *')
    a -= 1
