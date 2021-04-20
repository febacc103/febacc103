#5!
def fact(n1):
    #n1=int(input("enter a number"))
    fact=1
    for i in range(1,n1+1):
        fact*=i
        return(fact)
        f=fact(5)
print(f)