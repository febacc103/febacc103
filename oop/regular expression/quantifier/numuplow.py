# import re
# n= input("enter a word")
# x='([a-zA-Z]+\d{1}$)'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")
# 10. Write a Python program that matches a
# string that has an 'a' followed by anything, ending in 'b'?

import re
n= input("enter a string")
x='(^a[a-zA-Z0-9]$)'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")