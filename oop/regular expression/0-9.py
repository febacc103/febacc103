
import re

z= "[0-9]"  # either a,b,or c
matcher = re.finditer(z, "abtnm cccc@ 53kz")
for match in matcher:
        print(match.start())
        print(match.group())

