
import warnings


def body_param(name, unit, maximum):
    param = float(input('Enter your {} in {} '.format(name, unit)))
    if param < 0:
        raise ValueError(name + ' cannot be negative')
    if param == 0:
        raise ValueError(name + ' cannot be equal to zero')
    if param > maximum:
        warnings.warn('large value of' + name)
    return param


def man_weight():
    return body_param(name='weight', unit='kg', maximum=300)


def man_height():
    return body_param(name='height', unit='cm', maximum=250)


def calc_bmi(weight, height):
    return (weight * 10000) / (height ** 2)


def main():
    weight = man_weight()
    height = man_height()
    bmi = calc_bmi(weight, height)
    print('your bmi is ', bmi)


main()
