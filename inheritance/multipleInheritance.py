class ClassA:
    def print(self):
        print(" This is class A")


class ClassB:
    def print(self):
        print(" This is class B")


class ClassC(ClassB, ClassA):
    def printa(self):
        print(" This is class C")


c = ClassC
c.print(c)
