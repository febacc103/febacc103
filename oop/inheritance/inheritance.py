
#single inheritance
#-------------------

# class Parent:               #base class
#     parent_name="Arun"
#     def m1(self,age):
#         self.age=age
#         print("my name is",Parent.parent_name)
#         print(self.age)
#
# class child(Parent) :        #derived class is child class
#     def m2(self,cage):
#         self.cage=cage
#         print("parent name is",Parent.parent_name)
#         print(self.age)
#         print(self.cage)
#
# c=child()
# c.m1(23)
# c.m2(3)


class Parent:
    parent_name = "deepu"

    def m1(self, age):
        self.age = age
        print("my name is", Parent.parent_name)
        print(self.age)


class child(Parent):
    def m2(self, cname):
        self.cname = cname
        print("parent name is", Parent.parent_name)
        print("Parent age",self.age)
        print("child name:",self.cname)


c = child()
c.m1(40)
c.m2("Appu")