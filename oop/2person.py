class Person:
    def setval(self,name,age):
        self.age=age
        self.name=name
    def printvalue(self):
        print("name:",self.name)
        print("age:",self.age)
        
obj=Person()
obj.setval('feba',29)
obj.printvalue()