
lst=[11,14,15,18,22,23]
elm=int(input("enter element for search"))
lst.sort()
print(lst)
low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if (elm>lst[mid]):
        low=mid+1
    elif(elm<lst[mid]):
        upp=mid-1
    elif(elm==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")


