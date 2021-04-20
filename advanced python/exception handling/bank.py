# class Bank:
#     bname="sbi"
#     def acCreate(self,acno,name,):
#         #self.bname=bname
#         self.acno=acno
#         self.name=name
#         self.minimumbal=5000
#         self.balance=self.minimumbal
#
#     def deposit(self,amt):
#         self.balance+=amt
#         print("your",Bank.bname," account has been created the amount",amt)
#         print("your current balance=",self.balance)
#     def withdrow(self,amt):
#         if amt>self.balance:
#             print("insufficient balance")
#         else:
#             print("account debited with",amt)
#             self.balance-=amt
#             print("available balance=",self.balance)
#
#
#
# obj=Bank()
# obj.acCreate(125,"feba")
# obj.deposit(2500)
# obj.withdrow(1000)
#
#
# #static variable



class Bank:
     bname="sbi"
     def acCreate(self,ac_no,name):
        self.ac_no=ac_no
        self.name=name
        self.minimalbal=5000
        self.balance=self.minimalbal

     def deposit(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print("your",Bank.bname,"created the amount",self.minimalbal)
        print("your current balance",self.balance)

     def witdrow(self,amt):
         if amt>self.balance:
             print("insuffivient balance")
         else:
             print("account debicted with amount",amt)
             self.balance-=amt
             print("your current balance=",self.balance)


obj=Bank()
obj.acCreate(1234,"feba")
obj.deposit(10000)
obj.witdrow(50000)