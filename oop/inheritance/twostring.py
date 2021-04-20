class College:
    colgname="luminar"

    def __init__(self,name,roll):
        self.roll=roll
        self.name=name

    def printdetails(self):
        print("college name=",self.colgname)
        print("name of student=",self.name)
        print("rollno",self.roll)
    def __str__(self):
        return self.name+str(self.roll)
ob=College("anu",4)
print(ob)