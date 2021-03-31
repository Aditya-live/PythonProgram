"""
SQLite 3
"""

import sqlite3 as db

#print(type(db))

conn=db.connect(":memory:")

qry="create table student(roll no int primary key, name Text,branch Text)"

cur=conn.cursor()

cur.execute(qry)

"""rollno=input("Enter rollno")
name=input("Enter name")
branch=input("Enter branch")

qry="insert into student values(?,?,?)"
cur.execute(qry,(rollno,name,branch))
"""
#qry="insert into student values("+rollno",'"+name"','"+branch"')"
#cur.execute(qry)

qry="insert into student values(101,'James','CSE')"
cur.execute(qry)

qry="insert into student values(102,'Smith','CSE')"
cur.execute(qry)

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
