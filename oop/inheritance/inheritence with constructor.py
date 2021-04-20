# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def printval(self):
#         print("name",self.name)
#         print("age",self.age)
#
# class student(Person):
#     def __i

class   Animal:
    def __init__(self,Aname):
        self.name=Aname


    def printval(self):
        print("Animal name",self.Aname)


class Dog(Animal):
    def __init__(self,Dname,Aname):
        super().__init__(Aname)
        self.Dname=Dname
    def print(self):
        print(self.Dname)

obj=Animal("Dog")
obj.printval()
obj.print()

