#lst=[10,20,20,25,25,85,41,41,25,58]
#print(lst)
#lst1=set(lst)
#print(lst1)
#employee=[[1001,"arun",14000],[1002,"feba",144000],[1003,"john",18000],[1004,"blesson",16000]]
#print(employee)
#nested list
#for i in employee:
 #   print(i)
#arun
#feba
#for i in employee:   #nested list very important
 #   sum=0

  #  sum=sum+i[2]
   # if(i[2]>17000):
   #  print(i[1])
   #   print(sum)

lst=[10,10,10,15,16,15,17,18,29,16,15]
print("list1=", lst)
lst2=set(lst)
print(lst2)
employee=[[10,"feba",100000],[11,"blesson",50000],[13,"john",60000]]
print(employee)
sum=0
for i in employee:
    if(i[2]>60000):
        print(i[1])
    sum=sum+i[2]
print(sum)
