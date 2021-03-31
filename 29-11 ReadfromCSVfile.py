
fp=open("c://Python37//fileh//emp.txt",'r')
ftemp=open("c://Python37//fileh//temp.txt",'w')

#For printing a record
"""for rec in fp.readlines():
    print(rec,end=" ")

"""

#For searching a record
"""for rec in fp.readlines():
    lst=rec.split(',')
    if lst[0]==n:
        print(rec)
"""
#For adding a record
"""
eid=input("eid ")
fname=input("fname ")
lname=input('lname ')
email=input('email ')
hd=input('hd ')
jid=input('jid ')
sal=input('sal ')
comm=input('comm ')
mid=input('mid ')
did=input('did ')

lst=[eid,fname,lname,email,hd,jid,sal,comm,mid,did,"\n"]
rec=",".join(lst)

fp.write(rec)
"""

n=input("Enter id to delete")

for rec in fp.readlines():
    lst=rec.split(',')
    if lst[0]!=n:
        ftemp.write(rec)
    else:
        pass 
        
fp.close()
ftemp.close()

fp=open("c://Python37//fileh//emp.txt",'w')
ftemp=open("c://Python37//fileh//temp.txt",'r')

for rec in ftemp.readlines():
    fp.write(rec)

fp.close()
ftemp.close() 
