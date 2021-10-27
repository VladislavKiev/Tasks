# # list
#
# my_list = [1, 2, 3, True ,'wasd', None]
#
# # iteration
#
# for i in my_list:
#     print(i)
# print(my_list[0])
# print(my_list[-1])
#
# print('Lenght:', len(my_list))
#
# # string
#
# string = "Lorem"
#
# # iteration
#
# for i in string
#

# a = str(input('input string >>>'))
# b = input('symbol')
# count = 0
# for i in a:
#     if i == b:
#         count += 1
# else:
#     print('count', count)
#
# a = 10
# for i in range(a):
#     print("*" * i)

from random import randint

lst = [randint(1,100) for i in range(10)]

print(lst)

non_unique = [i for i in set(lst) if lst.count(i) > 1]

if len(non_unique) == 0:

   print("Повторяющихся элементов нет")

else:

   print(non_unique)
   

