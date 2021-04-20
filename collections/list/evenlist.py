lst=[]
evlst=[]
oddlst=[]
for i in range(50,101):
    lst.append(i)
for i in lst:
    if(i%2==0):
        evlst.append(i)
    else:
        oddlst.append(i)
print(lst)
print(evlst)
print(oddlst)
