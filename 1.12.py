# A random real number is given. Determine the maximum digit of this number. Execution example: 56.457 -> 7
# у тебя это же число (56.457) выводит 9, подумай ещё)

v = float(input('Input value >>> '))
vmax = 0
while v % 10 != 0:
    v = v*10
    # v = int(v)
    print(v)
v = int(v)
c= str(v)
for i in c:
    i = int(i)
    if i > vmax:
        vmax = i
print('max is', vmax)
