#operations
#union
#intersection
#difference
#set1={1,2,3,4,6,7,8}
#set2={4,6,5,6,7,8}

#union{1,2,3,4,5,6,7,8}
#set3=set1.union(set2)
#print(set3)

#intersection{4,6,7,8}
#set4=set1.intersection(set2)
#print(set4)

#difference
#set1-set2
#set5=set1.difference(set2)
#print(set5)
#set6=set2.difference(set1)
#print(set6)

set1={1,1,2,2,2,3,4,5}
set2={13,6,7,8,12,1,2,3,4}
print("set1=", set1)
print("set2=", set2)
set3=set1.union(set2)
print("union=",set3)
set4=set1.intersection(set2)
print("intersection=",set4)
set5=set1.difference(set2)
print("set1-set2=", set5)
set6=set2.difference(set1)
print("set2-set1", set6)