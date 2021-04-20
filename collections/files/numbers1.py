f=open("numbers","r")
list=[]
for num in f:
    list.append(int(num.rstrip("\n")))
print(list)
#\n remove rstrip
#remove first character lstrip
print(sum(list))
lstev=[]
lstod=[]
for i in list:
    if(i%2==0):
        lstev.append(i)
    else:
        lstod.append(i)
print(lstev)
print(sum(lstev))
print(lstod)
print(sum(lstod))