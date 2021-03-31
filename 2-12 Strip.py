fp=open("c:\\Python37\\fileh\\emp.txt",'r')

for rec in fp.readlines():
    lst=rec.split(',')
    if lst[10].strip('\n')=='50':
        print(rec)
