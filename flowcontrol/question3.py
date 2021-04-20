sex=input("enter sex(male,female,m,f):")
age=int(input("enter your age:"))
marg=input("your marriage status( y,n):")
if(sex.lower() in ("female","f")):
    print("only work in urban areas")

else:
     if(sex.lower() in ("male","m")):
       if(age>=20)&(age<=40):
           print("you can work anywhere")
if(age>=40)&(age<=60):
 print("you can work in urban areas only")
else:
    print("error")