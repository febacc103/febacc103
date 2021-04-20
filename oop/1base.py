#class:design pattern
#object:real world entity
#reference:name that refers a memory location of a object

class Person:
    def walk(self):#method inside class is walk   methods as functions
        print("person is walking")
    def run(self):
        print("person is running")
    def jump(self):
        print("person is juming")

#object creation
obj=Person()
obj.walk()
obj.run()
obj.jump()

ab= Person()                    #reference is ab    referece name always small letters
ab.walk()

