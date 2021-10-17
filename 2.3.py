# Given a list of numbers, you need to remove all occurrences of the number 20 from it.

list_3 = [20, 19, 20, 18, 20, 20]
x = 20
while x in list_3:
    list_3.remove(x)
print(list_3)
