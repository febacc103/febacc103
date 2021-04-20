#FIND SECOND LARGEST NUMBER
num1=int(input("enter first number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if(num1>num2)&(num1<num3):
    print("second largest number is",num1)
elif(num1>num3)&(num1<num2):
    print("second largest number is",num1)
elif(num2>num1)&(num2<num3):
    print("second large number is",num2)
elif(num2>num3)&(num2<num1):
    print("second largest number is:,num2")
elif(num3>num1)&(num3<num2):
    print("second largest number is:",num3)
elif(num3<num1)&(num3>num2):
    print("second largest number is:",num3)