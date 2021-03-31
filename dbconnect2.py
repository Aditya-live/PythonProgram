import pymysql as db

conn=db.connect("127.0.0.1","root","","python") # For no password write ""

def display():
    qry="select * from student"

    cur=conn.cursor()
    cur.execute(qry)
    rs=cur.fetchall()

    print("rollno\tname\tdob\t\taddress\t\tbranch\n--------------------------------------")
    for row in rs:
        for val in row:
            print(val, end="\t")
        print()  


#Search based on rollno
def search():
    rollno=input("Enter rollno")
    qry="select * from student where rollno=%s"   #using %s because we are passing rollno as string
    cur=conn.cursor()
    cur.execute(qry,(rollno,))
    rs=cur.fetchall()
    print(rs)

def insert():
    rollno=input("Enter rollno")
    name=input("Enter name")
    dob=input("Enter dob")
    address=input("Enter address")
    branch=input("Enter branch")

    qry="insert into student values(%s,%s,%s,%s,%s)"
    cur=conn.cursor()
    cur.execute(qry,(rollno,name,dob,address,branch,))
    rs=cur.fetchall()

display()

cur.close()        
conn.close()  
