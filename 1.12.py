# A random real number is given. Determine the maximum digit of this number. Execution example: 56.457 -> 7
# у тебя это же число (56.457) выводит 9, подумай ещё)

v = float(input('Input value >>> '))
str_v = str(v)
r_str_v = str_v.replace(".", "")
v_max = 0
for i in r_str_v:
    i = int(i)
    if i > v_max:
        v_max = i
print(v_max)
