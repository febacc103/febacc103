
from functools import reduce

lst=[10,20,30,40,50]
#SUM,MAX,MIN
total=reduce(lambda no1,no2:no1+no2,lst)
print(total)
mx=reduce(lambda no1,no2:no1 if (no1>no2)  else no2,lst)
print(mx)
min=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(min)