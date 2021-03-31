import sqlite3 as db


conn=db.connect("mydb")

qry="create table if not exists student(rollno int primary key, name Text,branch Text)"

cur=conn.cursor()

cur.execute(qry)

rollno=input("Enter rollno")
name=input("Enter name")
branch=input("Enter branch")

qry="insert into student values(?,?,?)"
cur.execute(qry,(rollno,name,branch))


conn.commit()

qry="select * from student"
cur.execute(qry)

rs=cur.fetchall()

print("Rollno\tname\tbranch\n----------------------")
for row in rs:
    for i in row:
        print(i,end="\t")
    print()    

cur.close()
conn.close()
