class Employe:
    def setval(self, id,name, salary):
        self.salary = salary
        self.name = name
        self.id=id

    def printvalue(self):
        print("id:", self.id)
        print("name:", self.name)
        print("salary:",self.salary)


obj = Employe()
obj.setval(1001,'feba', 50000)
obj.printvalue()