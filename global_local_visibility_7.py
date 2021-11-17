"""
global and local visibility area
"""

def outer_function():
    # local declaration
    def inner_function(a, b):
        print('internal function')
    print('external function')
    inner_function(2, 15)


outer_function()


def hyp(x, y):
    def pow_kat(a):
        return a * a
    return (pow_kat(x) + pow_kat(y)) ** 0.5


print(hyp(3, 4))


def valid_pass(password):
    def upper_case(string):
        count = 0
        for i in string:
            if 'A' <= i <= 'Z':
                count += 1
                if count == 2:
                    return  True
        return False

    def spec_symb(text):
        for i in text:
            if i in '!./;:&<>^':
                return True
        return False

    def len_pass(len_p):
        if len(len_p) >= 8:
            return True
        return False

    return upper_case(password) and spec_symb(password) and len_pass(password)


result = valid_pass('!FfFFFqwrty')
print(result)
