lst=[3,4,8]
lst1=[]
for i in lst:
    sum1=sum(lst)
    lst1.extend([sum1-i])
    #sum+=i
print(lst1)

lst2=[5,10,20]
lst3=[]
for i in lst2:
    sum2=sum(lst2)
    lst3.extend([sum2-i])
print(lst3)