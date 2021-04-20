class Parent:  # base class
    parent_name = "Arun"

    def m1(self, age):
        self.age = age
        print("my name is", Parent.parent_name)
        print(self.age)
class Mobile:
    def mob(self):
        print("i have 1+")

class child(Parent,Mobile):  # derived class is child class
    def m2(self, cage):
        self.cage = cage
        print("parent name is", Parent.parent_name)
        print(self.age)
        print(self.cage)


c = child()
c.m1(23)
c.m2(3)
c.mob()