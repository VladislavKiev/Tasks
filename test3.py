# def hello_world():
#     print('sdfgsfd')
#     print('fsafsf')
#     print('kjnkjn')
#
# hello_world()

# def print_numbers(limit):
#     print('lim= ', limit)
#     for i in range(limit):
#         print(i)
# print_numbers(15)

# def print_numbers(a,b):
#     for i in range(a):
#         if i == b:
#             continue
#         print(i)
# print_numbers(10, 7)

# def add_numbers(a,b):
#     return a + b
# c = add_numbers(3, 3 + 8)
# print(c)

# def s():
#     print('fasdfadfasdf')
# value = s()
# print('Res func', value)

# password = input("Enter pass >>>> ")
# def validate_pass():
#    if len(password) >= 8:
#       return False
#    for char in password:
#       if 'A' <= char <= 'Z':
#          return True
#    return False

# def validate_password(password):
#    first_condition = False
#    second_condition = False
#    if len(password) >= 8:
#       first_condition = True
#    for i in password:
#       if 'A' <= i <= 'Z':
#          second_condition = True
#          break
#    return first_condition and second_condition
# print(validate_password("hjgjgjgjgjgjgjgj"))

def check_upper(password, count_chars):
   res = False
   count = 0
   for i in password:
      if 'A' <= i <= 'Z':
         count += 1
      if count >= count_chars:
         return True
   return False

def validate_password(password):
   result_check_upper = check_upper(password, 2)
   if len(password) >= 8 and result_check_upper:
      return True
   else:
      return False
print('GjgjgjgjgjgGjg', validate_password('GjgjgjgjgjgGjg'))


# def f(x):
#    if x <= 0:
#       return x * 2
#    else:
#       return x * 3
#
# def main():
#    for i in range (-3, 4):
#       y = f(i)
#       print('f(' + str(i) + ')= ' + str(y))
#       if y == 6:
#          break
#    # else:
#    return y
# res = main()
# print(res)

# def hello(name):
#    if not name:
#       print('Empty')
#       return
#    else:
#       print('HEllo', name)
#       return name *2
# hello('')
# res = hello('Alex')
# c = hello('Python')
# print(c)
# hello(0)
#




