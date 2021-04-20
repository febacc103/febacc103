pattern="ACBCDBCA adf"
letter=pattern.split(" ")
print(letter)
dic={}
for i in pattern:
    if(i not in dic):
        dic[i]=1
    else:

       print(i)
       break