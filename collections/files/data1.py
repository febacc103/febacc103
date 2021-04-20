f=open("data","r")
dic={}
for lines in f:
    print(lines)
    words=lines.rstrip("\n").split(" ")
print(words)
for i in words:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

#1.location workers cound
#same age
#prfesstion count