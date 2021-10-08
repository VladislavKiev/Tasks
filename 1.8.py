# You are given two integers A and B. Print all numbers from A to B, inclusive, in ascending order if A <B, or in descending order otherwise.

a = int(input('Enter value A >>> '))
b = int(input('Enter value B >>> '))

if a > b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    for i in range(a, b + 1):
        print(i)
