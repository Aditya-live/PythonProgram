"""
Insert view and delete in Sqlite3
"""

import sqlite3 as db

conn=db.connect("mydb")

def viewall():
    qry="select * from student"
    cur.execute(qry)

    rs=cur.fetchall()

    print("Rollno\tname\tbranch\n------------------------------------")
    for row in rs:
        for i in row:
            print(i,end="\t")
        print()

qry="create table if not exists student(rollno int primary key, name Text,branch Text)"


cur=conn.cursor()
cur.execute(qry)

viewall()

rollno=input("Enter rollno")
name=input("Enter name")
branch=input("Enter branch")
qry="insert into student values(?,?,?)"
cur.execute(qry,(rollno,name,branch))
    
viewall()

rollno=input("Enter rollno to update")
name=input("Enter name")
branch=input("Enter branch")


qry="update student set name=?,branch=? where rollno=?"
if cur.execute(qry,(name,branch,rollno,)):
    conn.commit()
    print("Record updated")

    
viewall()

rollno=int(input("\nEnter rollno to remove"))

qry="delete from student where rollno=?"
if cur.execute(qry,(rollno,)):
    conn.commit()
    print("Record deleted")

cur.close()
conn.close()
