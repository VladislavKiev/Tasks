# Find the sum and product of the items in the list. Display the results

list_7 = [2, 9, 20, 2, 5, 6, 3]
s = 0
m = 1
for i in list_7:
    s = i + s
    m = i*m
print(s, m)
