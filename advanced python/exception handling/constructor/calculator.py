class Calc:
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
        self.sum=no1+no2
        self.sub=no1-no2
        self.mul=no1*no2
    def printval(self):
        print("add:",self.sum)
        print("sub:",self.sub)
        print("mul:",self.mul)
cl=Calc(15,10)
cl.printval()
