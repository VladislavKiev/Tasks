import warnings


class Human:
    first_n = 'default'

alex = Human()
alex.name = 'Alex'
alex.age = 23

petr = Human()
petr.name = 'Petr'
petr.age = 33

print('First person', alex.name, 'and his age', alex.age)
print('Second person', petr.name, 'and his age', petr.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if age < 16:
            warnings.warn('access limited')

    def info(self):
        print('{} is {} y.o'.format(self.name, self.age))
person_1 = Person('Vlad', 16)
person_2 = Person('Oleg', 55)

print(person_1.name, person_1.age)
print(person_2.name, person_2.age)

person_1.info()
Person.info(person_2)
