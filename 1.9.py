# With a for loop, display a rhombus

n = 10
m = 1
for i in range(n):
    print(n * "*" + "A" * m + n * "*")
    m += 2
    n -= 1
print('A' * (i * 2 + 3))
# print(n)
n = 10
m = 1
for i in range(n):
    print(m * "*" + "A" * (2 * n - 1) + m * "*")
    n -= 1
    m += 1
