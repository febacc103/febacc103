#attendence
num1=int(input("enter the total no.of classes held"))
num2=int(input("enter no.of class attend"))
num3=((num2/num1)*100)
if(num3>=75):
    print("you are eligible")
else:
    print("you could not allowed to write exam ")