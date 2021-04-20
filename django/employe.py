class Employe:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary

    def print_emp(self):
        print(self.ename)
e1=Employe(1000,"varun","developer",25000)
e2=Employe(1001,"arun","developer",26000)
e3=Employe(1002,"arjun","developer",25000)
e4=Employe(1003,"anoop","administrator",35000)