# 2. Create an example
# for three types of inheritance in one program by using Person
# as main class?

class Person:
    H_name="Cheruppukudiyil"
    def m1(self,pname):
        self.pname=pname
        print("House name:",Person.H_name)
        print("Person name:",self.pname)
class Parent(Person):
    def m2(self,fname):
        self.fname=fname
        print("Fathers name:",self.fname)

class Sibling(Parent):
    def m3(self,sname):
        self.sname=sname
        print("sibiling name:",self.sname)

obj=Sibling()
obj.m1("Feba")
obj.m2("C A Chacko")
obj.m3("John")