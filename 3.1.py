"""
1)Написать функцию которая делает следующее "При заданном целом числе n и кол-ве m посчитайте n + nn + nnn."
        Пример вызова
        calc_many_numbers(5 , 2) => 5 + 55 (60)
        calc_many_numbers(7 , 4) => 7 + 77 + 777 + 7777 (8638)
"""

def calc_many_numbers(value, iteration):
        a = str(value)
        b = str(value)
        for i in range(0, iteration):
                b = b + a
                value = value + int(b)
        return value
res = calc_many_numbers(5,0)
print(res)

