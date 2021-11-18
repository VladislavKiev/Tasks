"""
Write a function that accepts a dictionary with numeric values. It is necessary to multiply them all and display them on the screen.
"""


def mul_dict(d):
    print(dict.values(d))
    a = 1
    for i in dict.values(d):
        a = a * i
    return a


result = mul_dict({1: 6, 2: 5})
print(result)
