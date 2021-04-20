#regular expression....re
#used for pattern matching
#used for validation

import re   #re is a package

count = 0
matcher=re.finditer('ba','ababaaaaab')
for match in matcher:
    print("match avalable at",match.start())#return positions
    print("group=:",match.group())#which object find match
    count+=1
print("count=:",count)
