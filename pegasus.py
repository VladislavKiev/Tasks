"""
Pegasus
"""


class Bird:
    def fly(self):
        print('i`m flying', type(self))


class Horse:
    def run(self):
        print('i`m run', type(self))


class Pegasus(Horse, Bird):
    pass


def main():
    bird = Bird()
    horse = Horse()
    pegasus = Pegasus()
    bird.fly()
    horse.run()
    pegasus.fly()
    pegasus.run()


main()
