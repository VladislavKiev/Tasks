# mult appropriation variable
x, y, z = 1, 2, 3

a = 78
b = 82234
print(a, b)
a, b = b, a
print(a, b)


def abcd():
    return 1, 2, 3


a, b, c = abcd()
print(a, b, c)

some_list_gen = [i for i in range(10)]
print(some_list_gen)

some_list_gen = [i ** 2 for i in range(10)]
print(some_list_gen)

new_list = []
for i in range(10):
    new_list.append(i ** 2)
print(new_list)

some_list_gen = [i ** 2 for i in range(10) if i > 5]  # fast form
print(some_list_gen)

new_list = []  # slow form
for i in range(10):
    if i > 5:
        new_list.append(i ** 2)
print(new_list)


u = []
for i in '123sagsfag456':
    if '0' <= i <='9':
        u.append(int(i))
print(u)

r = '123sagsfag456'
some_list_gen = [int(i) for i in r if '0' <= i <= '9']
print(some_list_gen)

string = "Lorem ipsum aaaa bbb"
print(string)
sorted_string = sorted(string, reverse=True)
