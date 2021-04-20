# # def add(*args):
# #     sum=0
# #     for num in args:
# #       sum+=num
# #     return sum
# #
# #
# # res=add(10,20,30)
# # print(res)
# #
# # def print_person_detail(**kwargs):
# #     print(kwargs)
# #
# # print_person_detail(name="arun",place="idk",wplce="tvm")
#
#
# # lst=[10,40,30,67]
# # lst=sorted(lst,reverse=True)
# # print(lst)
# #
# #
# # lst=[10,40,30,67]
# # lst=sorted(lst,reverse=True)
# # print(lst)
#
# # def print_person_detail(*args):
# #     print(args)
# #
# # print_person_detail("arun","idk","tvm")
# #
# employees={
#     1000:{"name":"feba","desig":"developer","exp":1},
#     1001:{"name":"jeba","desig":"deve","exp":2},
#     1002:{"name":"john","desig":"ml","exp": 3},
#     1003:{"name":"feba","desig":"mln","exp":4}
# }
#
# #
# # eid=int(input("enter employee id:"))
# # if(eid in employees):
# #     print("eid exist")
# #     print(employees[eid]["name"])
# # else:
# #     print("eid not exist")
#
#
#
#     #create a function
#
#
#     #print_emp(eid=1000)
#     #emp_details(eid=1000,prop="design")
#
# def emp_details(**kwargs):
#     id=kwargs["eid"]
#     prop=kwargs["prop"]
#     if(id in employees):
#         print(employees[id]["name"])
#         print(employees[id][prop])
#     else:
#         print("not exist")
#
# emp_details(eid=1000,prop="desig")
#
#
#
#
# #employees
# #eid,ename,salary


#mysql-connector
#step1 import mysql module
#mysql -u root -pmpassword123
#establish connection
#step3 creat curser object
#execute sql qurries
#close db connection
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password@123"
)

cursor=db.cursor()
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
cursor.execute("show databases")
for i in cursor:
    print(i)
db.close()

