# 5 digits are entered alternately, display their sum (using for)

res = 0
for i in range(5):
    x = int(input('Enter value>>> '))
    res += x
print(res)
