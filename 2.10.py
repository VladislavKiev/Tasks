# Swap the largest and smallest list items

# почему, когда максимальное число в списке = 20, они не меняются?)
from random import randint

list_2 = []
for i in range(8):
    list_2.append(randint(0, 20))
print(list_2)
max_element = max(list_2)
list_2.index(max_element)
print(max_element)
min_element = min(list_2)
list_2.index(min_element)
print(min_element)
list_2[list_2.index(max(list_2))], list_2[list_2.index(min(list_2))] = list_2[list_2.index(min(list_2))], list_2[list_2.index(max(list_2))]
print(list_2)
