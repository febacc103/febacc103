#prime number
num=int(input("enter a number"))
if(num%2==0):
    print("no")
    if(num%3==0):
         print("no")
         if(num%4==0):
             print("no")
             if(num%5==0):
                 print("no")
                 if(num%7==0):
                     print("no")
else:
    print("prime")