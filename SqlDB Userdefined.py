"""
SQLite 3 user defined input
"""

import sqlite3 as db

#print(type(db))

conn=db.connect(":memory:")

qry="create table student(roll no int primary key, name Text,branch Text)"

cur=conn.cursor()

cur.execute(qry)

rollno=input("Enter rollno")
name=input("Enter name")
branch=input("Enter branch")

qry="insert into student values("+rollno+",'"+name+"','"+branch+"')"

rs=cur.fetchall()

print("Rollno\tname\tbranch\n----------------------")

for row in rs:
    for i in row:
        print(i,end="\t")
    print() 

cur.close()
conn.close()
