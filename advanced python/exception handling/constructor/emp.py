#employee
class Employe:
    cname="luminar"
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(Employe.cname)

em=Employe("feba",100,40000)
em.printval()

