lst=[5,6,7]
a=int(input("enter a number"))
try:
    print(lst[a])
except:
    print("exception")
finally:
    print("inside finally")