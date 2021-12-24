class Base:
    attr = 'Base attr'

    def method(self):
        print('Base method, current class is', self.__class__.__name__)

class X(Base):
    attr = 'Redefined attr'

    def get_superclass_attr(self):
        return super().attr

    def method(self):
        super().method()
        print('Child method, current class is', self.__class__.__name__)


def main():
    print('Base')
    print(Base.attr)
    base_instance = Base()
    base_instance.method()

    print()
    print('Child')
    print(X.attr)
    child_instance = X()
    child_instance.method()
    print(child_instance.get_superclass_attr())


main()
