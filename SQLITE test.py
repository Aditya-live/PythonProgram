

import sqlite3 as db

conn=db.connect(":memory:")

def viewall():
    cur=conn.cursor()
    qry="select * from test"
    cur.execute(qry)

    rs=cur.fetchall()

    print("ID\tName\n--------------------------------")
    for row in rs:
        for i in row:
            print(i,end="\t")
        print()
    cur.close()

def insert():
    cur=conn.cursor()
    idn=input("Enter id")
    name=input("Enter name")

    qry="insert into test values(?,?)"
    cur.execute(qry,(idn,name,))

    cur.close()

def search():
    idn=input("Enter name to search:")
    qry="select * from test where id==$s"
    cur=conn.cursor()
    cur.execute(qry,(idn,))
    rs=cur.fetchall()
    print(rs)
    cur.close()

    
qry="create table if not exists test(id int primary key, name Text)"

cur=conn.cursor()
cur.execute(qry)

insert()
viewall()
search()

conn.close()
