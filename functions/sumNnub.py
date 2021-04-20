#def sum()
#n=int(input("enter a number"))
#for i in range(1,n+1)
#sum=((n*(n+1))/2)
#print(sum)



def sumn():
    n=int(input("enter a number"))
    sum=((n*(n+1))/2)
    print(sum)
sumn()

def ev():
    n1=int(input("enter a number"))
    for i in range(1,n1+1):
        if(i%2==0):
            print(i)
ev()


def pr():
    n1=int(input("enter start"))
    n2=int(input("enter end"))
    for i in range(n1,n2):
        flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
        else:
            print(i)
pr()




