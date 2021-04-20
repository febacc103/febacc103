import re

x="^a"   #check starting with a
r="aaa pbc aaaaa acga"
matchar=re.finditer(x,r)
for match in matchar:
    print(match.start())
    print(match.group())