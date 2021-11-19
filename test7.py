# def custom(some_list, ext_obj):
#     for elem in ext_obj:
#         some_list.append(elem)
#     return some_list
#
#
# result = custom([1, 2, 3], 'some string')
#
# print(result, 'result list')
#
# def custom_2(some_list_2):
#     some_list_2.insert(1, 8)
#     return some_list_2
#
# result_2 = custom_2([1, 2, 3])
# print(result_2)
#
# result_2.remove(3)
# print(result_2)
#
# x = result_2.pop(2)
# print(result_2)
# print(x)
# print('pop', result_2.pop())
# print(result_2)
# result_2.clear()
# print(result_2)
#
#
# sequence = list(range(10))
# print(sequence)

u = []
for i in '1234wdsfawf234':
    if '0' <= i <= '9':
        u.append(int(i))
print(u)


a = '1234wdsfawf234'
b = [int(i) for i in a if '0' <= i <= '9']
print(b)
print(sum(b))

