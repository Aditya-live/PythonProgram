import pandas as pd
import pymysql as db

conn=db.connect("127.0.0.1","root",'',"python")
res=pd.read_sql("select * from student",conn)

print(res)
