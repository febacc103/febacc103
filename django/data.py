lst=[1,2,3,4,5,6,7,8,9,10,11,12]
# sq=[num**2 for num in lst]
# print(sq)
ev=[num for num in lst if num%2==0]
print(ev)
od=[num for num in lst if num%2!=0]
print(od)
# print(ev)
# lst=[1,2]
# lst1=[10,20]
# for i in lst:
#     for j in lst1:
#
#       print(i,j)
# pairs=[(i,j) for i in lst for j in lst1]
# print(pairs)