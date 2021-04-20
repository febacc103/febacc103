# 3. Create a Book class with instance Library_name, book_name,
# author, pages?

class Book:
    def m1(self,Library_name,book_name,author,pages):
        self.Library_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages

    def printval(self):
        print("Librsry nsme:",self.Library_name)
        print("book name:",self.book_name)
        print("author:",self.author)
        print("number of pages:",self.pages)

obj=Book()
obj.m1("National library","Fire of wings","Dr A P J Abdul kalam",180)
obj.printval()