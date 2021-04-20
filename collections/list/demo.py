#list
lst=[]   #define using suare bracket
st=list()
print(type(lst))
print(type(st))

lst1=[10,10.5,"feba",True]
print(lst1)
lst2=[10,10.5,"feba",True]
print(lst2)
lst3=["feba",10,True,10.5]
print(lst3)
#insertion order preserved
lst4=[10,7,9,100]
#     0 1  2 3
#indux value
print(lst4[3])
lst4[1]=50
print(lst4)

#list mutble
lst3[1]="john"
print(lst3)
