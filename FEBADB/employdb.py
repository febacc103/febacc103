import mysql.connector
db=mysql.connector.connect(
    user="root",
    host="localhost",
    passwd="password@123",
    database="pythonfeb",
    auth_plugin="mysql_native_password"

)
cursor=db.cursor()
f=open("employ")
for line in f:
    cursor.execute(tuple(line.rstrip("\n").split(",")))
    cursor.execute("insert into employee(eid,ename,desig,salary) values(%s,%s,%s,%s)")
   # cursor.execute(tuple(line.rstrip("\n").split(",")))
    #db.commit()
db.close()
