class ClassA:
    def print(self):
        print(" This is class A")


class ClassB(ClassA):
    def print(self):
        print(" This is class B")


class ClassC(ClassB):
    def print(self):
        print(" This is class C")