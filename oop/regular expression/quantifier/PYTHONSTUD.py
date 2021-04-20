import re
f1=open("validreg","w")
rule='([L][U][M]\d{2}[P][Y]\d{3}$)'
f=open("registernumber","r")

for num in f:
    number=num.rstrip("\n")
    print(number)
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        f1.write(number)
        f1.write("\n")



#combination of uppercase or lowercase numbers ending with a number