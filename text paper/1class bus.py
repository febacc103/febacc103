# 1. Create a child class  Bus that will inherit all
# of the variables and methods of Vehicle class?


class Vehicle:
    def m1(self,V_name):
        self.V_name=V_name
        print("vehicle name:",self.V_name)
class Bus(Vehicle):

    def m2(self,Bname):
        self.Bname=Bname
        print("Bus name:",self.Bname)

obj=Bus()
obj.m1("Bus")
obj.m2("Cochin")