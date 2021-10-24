"""
3) You accept from the user a sequence of numbers separated by commas. Make a list and tuple of these numbers.
"""

def seq():
    value = input('Enter value >>> ')
    value_str = value.split(',')
    arr = map(int, value_str)
    lst = list(arr)
    cor = tuple(lst)
    print(cor)
    print(lst)


seq()
