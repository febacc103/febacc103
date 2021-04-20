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
cursor.execute("use pythonfeb")
cursor.execute("show tables")
for j in cursor:
    print(j)
cursor.execute("select * from student")
for k in cursor:
    print(k)
#cursor.execute("use pythonfeb")
db.close()
