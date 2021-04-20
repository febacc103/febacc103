import mysql.connector
db=mysql.connector.connect(
    user="root",
    host="localhost",
    passwd="password@123",
    database="pythonfeb",
    auth_plugin="mysql_native_password"

)
cursor=db.cursor()
cursor.execute("insert into mytable(id,ename,salary) values(3,'blesson',35000)")
cursor.execute("update  mytable set salary='38000' where id=1")
cursor.execute("select * from mytable")
for i in cursor:
    print(i)
#cursor.execute("insert into mytable(id,ename,salary) values(3,'blesson',35000)")
db.close()