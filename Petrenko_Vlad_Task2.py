# 1. Empty lines must be removed from the list of lines.

str_list = ["first", "", "second", "", ""]
while '' in str_list:
    str_list.remove('')
print(str_list)

# 2. A list of numbers is given. Convert it to a list of squares of these numbers.

list_1 = [1, -2, 9, 4]
list_1 = [x * x for x in list_1]
print(list_1)

# 3. Given a list of numbers, you need to remove all occurrences of the number 20 from it.

list_3 = [20, 19, 20, 18, 20, 20]
x = 20
while x in list_3:
    list_3.remove(x)
print(list_3)

# 4. It is necessary to display the list in reverse order.

list_4 = [20, 19, 20, True, 'GGG', 20]
list_4 = list_4[::-1]
print(list_4)

# 5. Fill the list with one hundred zeros, except for the first and last elements, which must be equal to one

list_5 = [0] * 100
list_5[0] = list_5[-1] = 1
print(list_5)
print(len(list_5))

# 6. Form an ascending list of even numbers (number of elements 45)

a = [i for i in range(1, 91, 2)]
print(a)
print(len(a))

# 7. Find the sum and product of the items in the list. Display the results

list_7 = [2, 9, 20, 2, 5, 6, 3]
s = 0
m = 1
for i in list_7:
    s = i + s
    m = i*m
print(s, m)

# 8. Find the largest item in the list and display it

list_1 = [2, 9, 20, 2, 5, 6, 3]
value_max = max(list_1)
print(value_max)

list_2 = ["Aaaaa", "Bbbbbb", "CCcc"]
max_string = max(list_2, key=len)
print(max_string)

# 9. Determine if the list contains duplicate elements, if so, display this value\

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

# 10. Swap the largest and smallest list items
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

# 11. Write a program that takes as input a list of numbers in one line and displays on one line the values that are repeated in it more than once. The displayed numbers must not be repeated, the order of their output can be arbitrary.

list_2 = [int(i) for i in input().split()]
print(list_2)
uni = [i for i in set(list_2) if list_2.count(i) > 1]
if len(uni) == 0:
   print("No repeating elements")
else:
   print(uni)
