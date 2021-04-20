lst=[4,2,1,6,7,8]
#output[3,1,0,7,8,9]
updatelist=[]
for i in lst:
    if(i<5):
        updatelist.append(i-1)

    else:
        updatelist.append(i+1)
print(updatelist)

result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)