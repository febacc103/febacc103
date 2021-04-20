import re

n="febacc16@gmail.com"
#n=input("enter emailid:")
x="(\w+@\w+\.\w+$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")