#decorotors


#07/04/2021


#
# def sub(num1,num2):
#     if num1<num2:
#         ( num1,num2)=(num2,num1)
#     return num1-num2
#
# res=sub(20,100)
# print(res)

#
#
# def decorator_sub(fun):
#
#     def wrapper(num1,num2):
#         if num1 < num2:
#             ( num1,num2)=(num2,num1)
#         return fun(num1,num2)
#     return wrapper
#
# @decorator_sub
#
# def sub(num1,num2):
#
#     return num1-num2
#
# res=sub(20,100)
# print(res)


#2,10

def div_deco(fun):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return wrapper
@div_deco

def div(n1,n2):
    return n1/n2
res=div(2,5)
print(res)



#git and github 1.5 hr
#database 4hr
#422.4 m download