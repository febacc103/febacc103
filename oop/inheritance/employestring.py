class Employee:
    cpname="luminar tech"
    def empdet(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.salary)
        print(Employee.cmpname)
    def __str__(self):
        return str(self.id)
emp=Employee()
emp.empdet('arun',23,3,34000)
emp.printval()
