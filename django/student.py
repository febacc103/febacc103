class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name

s1=Student(100,"feba","bba",180)
print(s1)
s2=Student(101,"john","bba",190)
print(s2)
s3=Student(103,"saju","ba",185)
print(s3)
s4=Student(104,"blesson","ba",187)
print(s4)

studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)
studentlist.append(s4)
#print(studentlist)

studenttotal=list(map(lambda stud:stud.total,studentlist))
print(max(studenttotal))
