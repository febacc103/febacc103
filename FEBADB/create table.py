import mysql.connector

db=mysql.connector.connect(
    user="root",
    host="localhost",
    password="password@123",
    database="pythonfeb"
)

cursor=db.cursor()
# sql="create table employ(eid int,ename varchar(25),desig varchar(25),salary int)"
# cursor.execute(sql)
# db.close()
sql="insert into employ(eid,ename,desig,salary) values(100,'arun','developer,25000')"
cursor.execute(sql)

try:
    cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close

