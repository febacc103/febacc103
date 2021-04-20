#prime numbers from lower to upper
low=int(input("enter lower number"))
upp=int(input("enter upper limit"))

for i in range(low,upp+1):
    flag=0
    for j in range(2,i):
     if(i%j==0):
         flag=1
         break
    else:
         flag=0
    if(flag==0):
         print(i)

