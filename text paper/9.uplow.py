# 9. Write a Python program to find the sequences of one upper
# case letter followed by lower case letters?
#==============================================================

import re
s=input("enter a word:")
x='[A-Z]{1}[a-z]'
match=re.fullmatch(x,s)
if match is not None:
    print("yes")
else:
    print("no")