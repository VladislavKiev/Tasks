"""
Function conversion from dec to bin, oct, hex,
"""


def conv():
    number = int(input('enter value >>> '))
    print('binary       ', bin(number))
    print('octal        ', oct(number))
    print('hexadecimal  ', hex(number))


conv()
