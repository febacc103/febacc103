
import re

z= "\w"  # either a,b,or c
matcher = re.finditer(z, "abt c@5kz")
for match in matcher:
        print(match.start())
        print(match.group())