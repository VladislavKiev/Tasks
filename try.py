a = (3, 0, 'asd', 2.3)

for i in a:
    print(i, type(i))
    try:
        x = 2 / i
    except ValueError:
        print('Value error')
    except ZeroDivisionError as e:
        print('Zero Division error,', e)
    except Exception:
        print('Exception')
    else:
        print(x)


def contact_of_add(c, b):
    try:
        return float(c) + float(b)
    except:
        print('Except a and b as sting')
        return str(c) + str(b)


print(contact_of_add(3.5, '2.5'))
print(contact_of_add(5, '2a'))
print(contact_of_add("4f", "dfggf"))
print(contact_of_add(5, 3))


# def try_dv():
#     try:
#         first_value = float(input('Enter first value >>> '))
#         second_value = float(input('Enter second value >>> '))
#         res = first_value / second_value
#         print(res)
#     except ZeroDivisionError as error:
#         print('Error', error)
#
#
# try:
#     try_dv()
# except ValueError as error:
#     print("Error", error)


def try_divide_vlue():
    loop = True
    while loop:
        try:
            first_number = float(input('Enter first number >>> '))
            second_number = float(input('Enter second number >>> '))
            res = first_number / second_number
            # print(res)
            # break
        except (ValueError, ZeroDivisionError, Exception) as error:
            print('Error:', error)
            print('Please try again')
        else:
            print(res)
            break


try_divide_vlue()
