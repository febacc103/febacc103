import re

n="helloo"
x='\w{6}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")