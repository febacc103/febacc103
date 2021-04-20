#import re

#x="[abc]"  #either a,b,or c
#matcher = re.finditer(x, "abt c@5kz")
#for match in matcher:
 #   print(match.start())
 #   print(match.group())

  #  y = "[^abc]"  # except a,b,or c
  #  matcher = re.finditer(y, "abt c@5kz")
   # for match in matcher:
    #    print(match.start())
     #   print(match.group())

import re
x="[a-z]"  #either a,b,or c
matcher = re.finditer(x, "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())

import re

x="[A-Z]"  #either a,b,or c
matcher = re.finditer(x, "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())

import re

z= "\s"  # either a,b,or c
matcher = re.finditer(z, "abt c@5kz")
for match in matcher:
        print(match.start())
        print(match.group())