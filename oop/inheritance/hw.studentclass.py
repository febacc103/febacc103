# f=open("student","r")
# for i in f:
# print(i)

class Stud:
    def m(self,name,age):
       self.name=name
       self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
    def __str__(self):
        return(self.name)
f=open("student","r")
for line in f:
    data=line.split(" ")
    name=data[0]
    age=data[1]
    obj=Stud(name,age)
    obj.printval()
