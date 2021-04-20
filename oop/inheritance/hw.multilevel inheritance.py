#multilevel inheritence or hierarchiel inheritance
# class Parent:
#     pname="chacko"
#     def m1(self,age):
#       self.age=age
#
# class Child(Parent):
#     def m2(self,name):
#         self.name=name
#         print("parent name is:",Parent.pname)
#         print("child name is:", self.name)
#         print("parent age:",self.age)
#
#
# class Subchild(Child):
#     def m3(self):
#        print("parent name:",self.name)
#
#
# obj=Subchild()
# obj.m3()
# obj.m2("vidya")
# obj.m1(28)

# obj=Subchild()
# obj.m1(58)
# obj.m2("veena")
# obj.m3()
# class Vehicle:
#     def m1(self,vname):
#         self.vname=vname
#
# class Bus( Vehicle):
#     def m2(self,bname):
#         self.bname=bname
#         print(self.vname)
#         print(self.bname)
#
# obj=Bus()
# obj.m1("bus")
# obj.m2("cochin")


# class Person:
#     homename="kripabhavan"
#     def m1(self,name,age):
#       self.name=name
#       self.age=age
#       print("Person name is:", self.name)
# class Parent(Person):
#     def m2(self,pname):
#         self.pname=pname
#         print("House name is:",Person.homename)
#
#         print("parent name is:",self.pname)
#
#
# class Sibling(Parent):
#     def m3(self,sname):
#         self.sname=sname
#         print(" sibling name:",self.sname)
#
#
# obj=Sibling()
#
# obj.m1("anju",28)
# obj.m2("mathew")
# obj.m3("veena")

#3. Create a Book class with instance Library_name, book_name, author, pages?



class Book:

    def m1(self, Library_name, book_name,author,pages):

      self. Library_name= Library_name
      self. book_name= book_name
      self.author=author
      self.pages=pages

    def printval(self):
        print("Library name:",self. Library_name)
        print("Book name",self. book_name)
        print("Author name:",self.author)
        print("No. of pages", self.pages)

obj=Book()

obj.m1("National library","fire of wings","Dr. A P J Abdul Kalam",180)
obj.printval()