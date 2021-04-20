#single inheritance

class Company:  # base class
    comp_name = "luminar"

    def m1(self, location):
        self.location = location
        print("company name is", Company.comp_name)
        print(self.location)


class emp(Company):  # derived class is child class
    def m2(self, name,salary):
        self.name = name
        self.salary=salary
        print("company name is", Company.comp_name)
        print("Employee name:",self.name)
        print("salary:",self.salary)


c = emp()
c.m1("kakkanadu")
c.m2("feba",40000)