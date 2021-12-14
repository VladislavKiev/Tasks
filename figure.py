"""
Figure
"""


class Figure:
    def __init__(self, a):
        self.side = a


class Square(Figure):
    def draw(self):
        for _ in range(self.side):
            print('*  ' * self.side)


class Triangle(Figure):
    def draw(self):
        side = self.side
        for i in range(side):
            print('*  ' * (i + 1))


def main():
    a = int(input('enter side >>> '))
    square = Square(a)
    triangle = Triangle(a)
    print()
    square.draw()
    triangle.draw()


main()
