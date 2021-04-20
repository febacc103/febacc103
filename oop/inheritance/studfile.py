# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def printvalue(self):
#         print("name:",self.name)
#         print("age:",self.age)
#     def __str__(self):
#         return self.name
# f=open("student","r")
# for line in f:
#     data=line.split(",")
#     name=data[0]
#     age=data[1]
#     obj=Student(name,age)
#     print(obj)
#     obj.printvalue()



class Student:
    def __init__(self,name,id,course,mark):
        self.name=name
        self.id=id
        self.course=course
        self.mark=mark

    def printvalue(self):
        print("name:",self.name)
        print("id:",self.id)
        print("course:", self.course)
        print("mark:", self.mark)
    def __str__(self):
        return self.name
f=open("marktest","r")
for line in f:
    data=line.split(",")
    name=data[0]
    id=data[1]
    course = data[2]
    mark = int(data[3])
    obj=Student(name,id,course,mark)
    #print(obj)
    #for i in (data[3]):
     #if(i>i+1):
    k=[]
    #k=k.append[mark]
    k.extend([mark])
    #print(k)
   # print(max[k])
    #obj.printvalue()

    1.
    Create
    a
    child


    class Bus that will inherit all of the variables and methods of Vehicle class ?


