#sum of eve number
#sum of odd numbers

low=int(input("enter lower number"))
upp=int(input("enter upper limit"))
evsum=0
odsm=0
for i in range(low,upp+1):
    if(i%2==0):
        evsum+=i
    else:
        odsm+=i
print(evsum)
print(odsm)
