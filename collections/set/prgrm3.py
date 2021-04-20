#homework
#lst=[1,2,3,4,5,6]
#for i in lst:#6
#pairs
#(2,4)
#5
#(2,3)(1,4)


#dictionary and file

lst=[1,2,3,4,5,6]
for i in lst:
    for j in lst:
        flag=0
        if(i+j==6):
            flag=1
        if(flag>0):
         print(i,j)