"""
Create a dictionary in which the keys will be numbers from 1 to 10, and the values will be the same numbers, cubed. Use a generator expression
"""


d = {i: i ** 3 for i in range(1, 11)}
print(d)
print(dict.keys(d))
print(dict.values(d))
