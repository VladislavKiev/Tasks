# Write a program that takes as input a list of numbers in one line and displays on one line the values ​​that are repeated in it more than once. The displayed numbers must not be repeated, the order of their output can be arbitrary.

list_2 = [int(i) for i in input().split()]
print(list_2)
uni = [i for i in set(list_2) if list_2.count(i) > 1]
if len(uni) == 0:
   print("No repeating elements")
else:
   print(uni)
