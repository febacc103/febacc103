# 6. Create objects of the following file and print the details of
# student with maximum mark? anu,1,bca,200 rahul,2,bba,177 vinod,3,
# bba,187 ajay,4,bca,198 maya,5, bba, 195

class Student:
    def __init__(self,name,no,course,mark):
        self.name=name
        self.no=no
        self.course=course
        self.mark=mark
    def printval(self):
        print("name:",self.name)
        print("no:",self.no)
        print("Branch:",self.course)
        print("mark:",self.mark)

f=open("6max_mark","r")
for line in f:
    data=line.split(",")
    name=data[0]
    no=data[1]
    course=data[2]
    mark=data[3]

    obj=Student(name,no,course,mark)
   # print(max(int(mark)))
    if (int(mark) > 198):
       obj.printval()
