#employee
# class Employe:
#     cname="luminar"
#     def emp(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary
#     def printval(self):
#         print(self.name)
#         print(self.id)
#         print(self.salary)
#         print(Employe.cname)
# em=Employe()
# em.emp("feba",100,40000)
# em.printval()
# emp1=Employe()
# emp1.emp("")




class Employe:
    cname="luminar"
    def emp(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print("name:",self.name)
        print("age=",self.age)
        print("salary=",self.salary)

obj=Employe()
obj.emp("Feba",29,50000)
obj.printval()
obj=Employe()
obj.emp("john",24,40000)
obj.printval()