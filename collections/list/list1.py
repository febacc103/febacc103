#binary search
#list
lst=[]
lst.extend([10,20,30,40])
print(lst)
n=int(input("enter a number"))
flag=0
for i in lst:
    if(i==n):
        flag=1
        break
    else:
        pass
if(flag>0):#linear search
    print("element found")
else:
    print("element not found")




#binay search