#07/4/2021
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return Book(self.pages-other.pages)
    def __sub__(self,other):
        return Book(self.pages+other.pages)
    def __mul__(self):
        return "overloading multiplication"
    def __truediv__(self):
        return "overloading division"
    def __str__(self):
        return str(self.pages)

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(500)
print(b1+b2+b3+b4)
print(b1-b2)
#+ arithmetic operator 10+10=20
#hello+hai concatination
