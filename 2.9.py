# Determine if the list contains duplicate elements, if so, display this value\

from random import randint

list_2 = []
for i in range(8):
    list_2.append(randint(0, 3))
print(list_2)
print(*filter(lambda x: list_2.count(x) > 1, list_2))
print(*set([i for index, i in enumerate(list_2) if i in list_2[index + 1:]]))

uni = [i for i in set(list_2) if list_2.count(i) > 1]
if len(uni) == 0:
   print("No repeating elements")
else:
   print(uni)
