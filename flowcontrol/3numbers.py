num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
if(num1>num2)&(num1>num3):
    print("gratest number is",num1)
elif(num2>num1)&(num2>num3):
    print(num2)
else:
    print(num3)