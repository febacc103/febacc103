# 7. Create a valid phone numbers file from the following file?
# +915678905432 +914567890321 765432167 123450987765 +919976532456

import re
f2=open("vph","w")
lst=[]
rule='[+][9][1]\d{10}$'
f=open("7phno","r")
for line in f:
    match=re.fullmatch(rule,line.rstrip("\n"))
    if match is not None:
        f2.write(line)
        f2.write("\n")