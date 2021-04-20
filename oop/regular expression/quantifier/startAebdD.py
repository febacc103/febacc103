# import re
# n= input("enter a word:")
# x='(^a[a-zA-Z0-9-+=.,/]*b$)'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")


#9. Write a Python program to find the sequences o
# f one upper case letter followed by lower case letters?
import re
n= input("enter a word:")
x='([A-Z]{1}[a-z]$)'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")