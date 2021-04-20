#binary search #lst.sort
#algorithm

#1).sort the array

#2.define a veriable low
   #low=0
   #upper=length of list-1=len(lst)-1

#3.claculate mid
#mid=(low+mid)//2         (0+4)//2=2

   #3 coditions check

    #if(element>lst[mid])
    #low=mid+1

   #second condition

   #if(element<lst[mid])
   #upp=mid-1
  #if search element==lst[mid]
  #element found
element=int(input("enter a element for search"))
lst=[45,20,50,40]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
mid=(low+upp)//2
print(mid)
if(element>lst(mid)):
  low=mid+1
if(element<lst(mid)):
 upp=mid-1
if(element==list(mid)):
    print("element found")
else:
           print("element not found")


