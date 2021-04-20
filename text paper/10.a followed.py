# 10. Write a Python program that matches a string that has an 'a'
# followed by anything, ending in 'b'?
#==================================================================

import re
s=input("enter a word:")
x='^a[a-zA-Z0-9W]*b$'
match=re.fullmatch(x,s)
if match is not None:
    print("valued")
else:
    print("false ")