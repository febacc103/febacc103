class Bank:
    def cCreate(self,acno,name,bname):
        self.bname=bname
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal


    def deposit(self,amt):
        self.balance+=amt
        print("")