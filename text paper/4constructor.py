# 4. Create an Animal class using constructor and build a child
# class for Dog?

class Animal:
    def __init__(self,aname):
        self.aname=aname
    def printval(self):
        print("animal name:",self.aname)

class Dog(Animal):
    def __init__(self,D_name,aname):
        super().__init__(aname)
        self.D_name=D_name
    def printval2(self):
        print("Dog name:",self.D_name)

obj=Dog("dobarman","dog")
obj.printval()
obj.printval2()