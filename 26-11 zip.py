"""zip in python """

lst1=["name","age", "sal"]
lst2=["james",'25',45000]

d={}
for k,v in zip(lst1,lst2):
    d[k]=v

for k,v in d.items():
    print(k,"->",v)
