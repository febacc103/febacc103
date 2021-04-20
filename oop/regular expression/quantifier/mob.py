import re
f2=open("validmob",'a')
rule='([+][9][1]\d{10})'
f=open("mob","r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher is not None:
        f2.write(number)
        f2.write("\n")

        Overriding is the
        property
        of
        a


        # class to change the implementation of a method
        # provided by one of its base classes....Method
        # overriding is thus a part of the inheritance
        # mechanism.In Python method overriding occurs
        # by simply defining in the child class a method with
        # the same name of a method in the parent class