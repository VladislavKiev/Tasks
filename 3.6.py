"""
6) Task. Print the multiplication table of the number M in the range from number a to number b. The numbers M, a and b are entered by the user.
            For example:
If M = 4, a = 2, b = 9, then the result will be:
4x2 = 8 4x3 = 12 4x4 = 16 4x5 = 20 4x6 = 24 4x7 = 28 4x8 = 32 4x9 = 36
"""

def mult():
    M = int(input('enter the number to be multiplied >>> '))
    a = int(input('enter value "a" >>> '))
    b = int(input('enter value "b" >>> '))
    if a <= 0 or b <= 0 or b <= a:
        print("Enter correct value")
    else:
        for a in range(a, b+1):
            print(M, "x", a, "=", M * a)
            a += 1
mult()
