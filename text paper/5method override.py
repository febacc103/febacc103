# 5. What is method overriding give an example using Books class?
#===============================================================

# Overriding is the property of a class to change
# the implementation of a method provided by one
# of its base classes. ... Method overriding is thus
# a part of the inheritance mechanism. In Python
# method overriding occurs by simply defining in
# the child class a method with the same name of a method
# in the parent class.
#=============================================================

class Book:
    def m1(self,bname):
        self.bname=bname
        print("branch:",self.bname)
class Sbook(Book):
    def m2(self,sbname):
        self.sbname=sbname
        print("book name:",self.sbname)

obj=Sbook()
obj.m1("science")
obj.m2("chemistry")