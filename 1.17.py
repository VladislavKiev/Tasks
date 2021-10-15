# Write a program that asks for three integers a, b, and x and prints True if x is between a and b, or False otherwise.

a = int(input('Enter value a >>> '))
b = int(input('Enter value b >>> '))
x = int(input('Enter value x >>> '))

if a < x < b:
    print('True')
else:
    print('False')
