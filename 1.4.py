# From a list of random numbers, identify and display the odd numbers.
from random import randint

lst_1 = [randint(0, 12) for i in range(8)]
print(lst_1)
# for x in lst_1:
#     print(x)
for x in lst_1:
    if x % 2 != 0:
        print('odd value', x)
