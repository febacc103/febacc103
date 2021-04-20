
import re

x="a{2,3}"   #miimum 2 and maximum 3
r="aaa abc aaaaa acga"
matchar=re.finditer(x,r)
for match in matchar:
    print(match.start())
    print(match.group())