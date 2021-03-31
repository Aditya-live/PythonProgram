Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import xlrd
>>> import openpyexcel
>>> 
>>> EMS=pd.ExcelFile('C://Python37//Prog//files//EMS.xlsx')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    EMS=pd.ExcelFile('C://Python37//Prog//files//EMS.xlsx')
NameError: name 'pd' is not defined
>>> import pandas as pd
>>> 
>>> EMS=pd.ExcelFile('C://Python37//Prog//files//EMS.xlsx')
>>> EMS
<pandas.io.excel._base.ExcelFile object at 0x0000028A4E135DA0>
>>> emp=ps.read_excel(EMS,'Sheet1')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    emp=ps.read_excel(EMS,'Sheet1')
NameError: name 'ps' is not defined
>>> emp=pd.read_excel(EMS,'Sheet1')
>>> dpt=pd.read_excel(EMS,'Sheet2')
>>> loc=pd.read_excel(EMS,'Sheet3')
>>> 
>>> emp
     Employee_Id       Name  Hire_Date  ... Salary  Manager_Id  Department_Id
0            100     Steven 1987-06-17  ...  24000         NaN           90.0
1            101      Neena 1989-09-21  ...  17000       100.0           90.0
2            102        Lex 1993-01-13  ...  17000       100.0           90.0
3            103  Alexander 1990-01-03  ...   9000       102.0           60.0
4            104      Bruce 1991-05-21  ...   6000       103.0           60.0
..           ...        ...        ...  ...    ...         ...            ...
105          205    Shelley 1994-06-07  ...  12000       101.0          110.0
106          206    William 1994-06-07  ...   8300       205.0          110.0
107          301      Smith 1989-06-17  ...  15000       100.0           90.0
108          302      _Paul 1993-02-12  ...  20000       100.0          110.0
109          303      Pa%ul 1993-02-12  ...  20000       100.0          110.0

[110 rows x 7 columns]
>>> dpt
    Department_Id       Department_Name  Manager_Id  Location_Id
0              10        Administration       200.0         1700
1              20             Marketing       201.0         1800
2              30            Purchasing       114.0         1700
3              40       Human Resources       203.0         2400
4              50              Shipping       121.0         1500
5              60                    IT       103.0         1400
6              70      Public Relations       204.0         2700
7              80                 Sales       145.0         2500
8              90             Executive       100.0         1700
9             100               Finance       108.0         1700
10            110            Accounting       205.0         1700
11            120              Treasury         NaN         1700
12            130         Corporate Tax         NaN         1700
13            140    Control And Credit         NaN         1700
14            150  Shareholder Services         NaN         1700
15            160              Benefits         NaN         1700
16            170         Manufacturing         NaN         1700
17            180          Construction         NaN         1700
18            190           Contracting         NaN         1700
19            200            Operations         NaN         1700
20            210            IT Support         NaN         1700
21            220                   NOC         NaN         1700
22            230           IT Helpdesk         NaN         1700
23            240      Government Sales         NaN         1700
24            250          Retail Sales         NaN         1700
25            260            Recruiting         NaN         1700
26            270               Payroll         NaN         1700
>>> loc
    Location_Id             Street_Address  ...    State_Province Country_Id
0          1000       1297 Via Cola di Rie  ...               NaN         IT
1          1100    93091 Calle della Testa  ...               NaN         IT
2          1200           2017 Shinjuku-ku  ...  Tokyo Prefecture         JP
3          1300            9450 Kamiya-cho  ...               NaN         JP
4          1400        2014 Jabberwocky Rd  ...             Texas         US
5          1500        2011 Interiors Blvd  ...        California         US
6          1600             2007 Zagora St  ...        New Jersey         US
7          1700            2004 Charade Rd  ...        Washington         US
8          1800            147 Spadina Ave  ...           Ontario         CA
9          1900            6092 Boxwood St  ...             Yukon         CA
10         2000        40-5-12 Laogianggen  ...               NaN         CN
11         2100         1298 Vileparle (E)  ...       Maharashtra         IN
12         2200      12-98 Victoria Street  ...   New South Wales         AU
13         2300         198 Clementi North  ...               NaN         SG
14         2400             8204 Arthur St  ...               NaN         UK
15         2500            Magdalen Centre  ...            Oxford     Oxford
16         2600          9702 Chester Road  ...        Manchester         UK
17         2700      Schwanthalerstr. 7031  ...           Bavaria         DE
18         2800      Rua Frei Caneca 1360   ...         Sao Paulo         BR
19         2900    20 Rue des Corps-Saints  ...            Geneve         CH
20         3000          Murtenstrasse 921  ...                BE         CH
21         3100  Pieter Breughelstraat 837  ...           Utrecht         NL
22         3200      Mariano Escobedo 9991  ...  Distrito Federal         MX

[23 rows x 6 columns]
>>> 
=========== RESTART: C:/Python37/Prog/26-11 pandas read in sql.py ===========
Traceback (most recent call last):
  File "C:/Python37/Prog/26-11 pandas read in sql.py", line 4, in <module>
    conn=db.connect("127.0.0.1","root","python")
  File "C:\Python37\lib\site-packages\pymysql\__init__.py", line 94, in Connect
    return Connection(*args, **kwargs)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 325, in __init__
    self.connect()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 599, in connect
    self._request_authentication()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 861, in _request_authentication
    auth_packet = self._read_packet()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 684, in _read_packet
    packet.check_error()
  File "C:\Python37\lib\site-packages\pymysql\protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Python37\lib\site-packages\pymysql\err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")
>>> 
=========== RESTART: C:/Python37/Prog/26-11 pandas read in sql.py ===========
Traceback (most recent call last):
  File "C:/Python37/Prog/26-11 pandas read in sql.py", line 4, in <module>
    conn=db.connect("127.0.0.1","root","python")
  File "C:\Python37\lib\site-packages\pymysql\__init__.py", line 94, in Connect
    return Connection(*args, **kwargs)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 325, in __init__
    self.connect()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 599, in connect
    self._request_authentication()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 861, in _request_authentication
    auth_packet = self._read_packet()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 684, in _read_packet
    packet.check_error()
  File "C:\Python37\lib\site-packages\pymysql\protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Python37\lib\site-packages\pymysql\err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")
>>> 
=========== RESTART: C:/Python37/Prog/26-11 pandas read in sql.py ===========
Traceback (most recent call last):
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1595, in execute
    cur.execute(*args)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 170, in execute
    result = self._query(query)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 328, in _query
    conn.query(q)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 517, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 732, in _read_query_result
    result.read()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 1075, in read
    first_packet = self.connection._read_packet()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 684, in _read_packet
    packet.check_error()
  File "C:\Python37\lib\site-packages\pymysql\protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Python37\lib\site-packages\pymysql\err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1146, "Table 'python.stduents' doesn't exist")

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Python37/Prog/26-11 pandas read in sql.py", line 5, in <module>
    res=pd.read_sql("select * from stduents",conn)
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 410, in read_sql
    chunksize=chunksize,
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1645, in read_query
    cursor = self.execute(*args)
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1610, in execute
    raise_with_traceback(ex)
  File "C:\Python37\lib\site-packages\pandas\compat\__init__.py", line 47, in raise_with_traceback
    raise exc.with_traceback(traceback)
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1595, in execute
    cur.execute(*args)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 170, in execute
    result = self._query(query)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 328, in _query
    conn.query(q)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 517, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 732, in _read_query_result
    result.read()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 1075, in read
    first_packet = self.connection._read_packet()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 684, in _read_packet
    packet.check_error()
  File "C:\Python37\lib\site-packages\pymysql\protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Python37\lib\site-packages\pymysql\err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pandas.io.sql.DatabaseError: Execution failed on sql 'select * from stduents': (1146, "Table 'python.stduents' doesn't exist")
>>> 
=========== RESTART: C:/Python37/Prog/26-11 pandas read in sql.py ===========
Traceback (most recent call last):
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1595, in execute
    cur.execute(*args)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 170, in execute
    result = self._query(query)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 328, in _query
    conn.query(q)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 517, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 732, in _read_query_result
    result.read()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 1075, in read
    first_packet = self.connection._read_packet()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 684, in _read_packet
    packet.check_error()
  File "C:\Python37\lib\site-packages\pymysql\protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Python37\lib\site-packages\pymysql\err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1146, "Table 'python.students' doesn't exist")

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Python37/Prog/26-11 pandas read in sql.py", line 5, in <module>
    res=pd.read_sql("select * from students",conn)
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 410, in read_sql
    chunksize=chunksize,
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1645, in read_query
    cursor = self.execute(*args)
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1610, in execute
    raise_with_traceback(ex)
  File "C:\Python37\lib\site-packages\pandas\compat\__init__.py", line 47, in raise_with_traceback
    raise exc.with_traceback(traceback)
  File "C:\Python37\lib\site-packages\pandas\io\sql.py", line 1595, in execute
    cur.execute(*args)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 170, in execute
    result = self._query(query)
  File "C:\Python37\lib\site-packages\pymysql\cursors.py", line 328, in _query
    conn.query(q)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 517, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 732, in _read_query_result
    result.read()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 1075, in read
    first_packet = self.connection._read_packet()
  File "C:\Python37\lib\site-packages\pymysql\connections.py", line 684, in _read_packet
    packet.check_error()
  File "C:\Python37\lib\site-packages\pymysql\protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Python37\lib\site-packages\pymysql\err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pandas.io.sql.DatabaseError: Execution failed on sql 'select * from students': (1146, "Table 'python.students' doesn't exist")
>>> 
=========== RESTART: C:/Python37/Prog/26-11 pandas read in sql.py ===========
   rollno     name         dob   address branch
0     100   Aditya  1997-01-01     Solan    CSE
1     101  Ankisha  1999-01-04     Narag    CSE
2     102    Rohit  0199-03-10  Parwanoo    CSE
>>> 
========= RESTART: C:/Python37/Prog/Assignment 13 Pandas/diabetes.py =========
     Pregnancies  Glucose  ...  Age  Outcome
0              6      148  ...   50        1
1              1       85  ...   31        0
2              8      183  ...   32        1
3              1       89  ...   21        0
4              0      137  ...   33        1
..           ...      ...  ...  ...      ...
763           10      101  ...   63        0
764            2      122  ...   27        0
765            5      121  ...   30        0
766            1      126  ...   47        1
767            1       93  ...   23        0

[768 rows x 9 columns]
>>> 
