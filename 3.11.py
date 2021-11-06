"""
The function takes two lists. It is necessary to return from the function a dictionary from them in such a way that the elements of the first list are keys, and the elements of the second are, respectively, the values of our dictionary.
"""


def new_dict(keys, values):
    d = dict(zip(keys, values))
    print(d)


new_dict((1, 2, 3, 4), (5, 6, 7, 8))
