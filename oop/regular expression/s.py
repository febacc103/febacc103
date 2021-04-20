
import re

z= "\s"  # either a,b,or c
matcher = re.finditer(z, "abtnm cccc@ 5kz")
for match in matcher:
        print(match.start())
        print(match.group())