def custom(*a):
    # print(a, type(a))
    if not a:
        return
        # raise ValueError
    min_ = a[0]
    for i in a:
        if i < min_:
            min_ = i
    return min_


__ = print
res = custom(123, -1, 45, 67)
__(res)
res = custom(123, -1)
__(res)
res = custom()
__(res)

# print('res', res)
