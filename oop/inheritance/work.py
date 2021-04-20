class Work:
    def __init__(self,name,id,course,mark):
        self.name=name
        self.id=id
        self.course=course
        self.mark=mark

    def printvalue(self):
        print("name:",self.name)
        print("id:",self.id)
        print("course:",self.course)
        print("mark:",self.mark)
    def __str__(self):
        return self.name
f=open("work","r")
for line in f:
    data=line.split(",")
    name=data[0]
    id=data[1]
    course=data[2]
    mark=int(data[3])
    obj=Work(name,id,course,mark)
   # print(obj)
    if(mark>190):
     obj.printvalue()