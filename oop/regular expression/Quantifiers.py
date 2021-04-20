# a+ a including group
import re

x="c+"   #a including group
r="aaa abc aaaaa acga"
matchar=re.finditer(x,r)
for match in matchar:
    print(match.start())
    print(match.group())