Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> 
>>> for i dir(pd):
	
SyntaxError: invalid syntax
>>> for i dir(pd):
	
SyntaxError: invalid syntax
>>> for i in dir(pd):
	print(i)

	
Categorical
CategoricalDtype
CategoricalIndex
DataFrame
DateOffset
DatetimeIndex
DatetimeTZDtype
ExcelFile
ExcelWriter
Float64Index
Grouper
HDFStore
Index
IndexSlice
Int16Dtype
Int32Dtype
Int64Dtype
Int64Index
Int8Dtype
Interval
IntervalDtype
IntervalIndex
MultiIndex
NaT
NamedAgg
Period
PeriodDtype
PeriodIndex
RangeIndex
Series
SparseArray
SparseDataFrame
SparseDtype
SparseSeries
Timedelta
TimedeltaIndex
Timestamp
UInt16Dtype
UInt32Dtype
UInt64Dtype
UInt64Index
UInt8Dtype
__builtins__
__cached__
__doc__
__docformat__
__file__
__getattr__
__git_version__
__loader__
__name__
__package__
__path__
__spec__
__version__
_config
_hashtable
_lib
_libs
_np_version_under1p14
_np_version_under1p15
_np_version_under1p16
_np_version_under1p17
_tslib
_typing
_version
api
array
arrays
bdate_range
compat
concat
core
crosstab
cut
date_range
datetime
describe_option
errors
eval
factorize
get_dummies
get_option
infer_freq
interval_range
io
isna
isnull
lreshape
melt
merge
merge_asof
merge_ordered
notna
notnull
np
offsets
option_context
options
pandas
period_range
pivot
pivot_table
plotting
qcut
read_clipboard
read_csv
read_excel
read_feather
read_fwf
read_gbq
read_hdf
read_html
read_json
read_msgpack
read_parquet
read_pickle
read_sas
read_spss
read_sql
read_sql_query
read_sql_table
read_stata
read_table
reset_option
set_eng_float_format
set_option
show_versions
test
testing
timedelta_range
to_datetime
to_msgpack
to_numeric
to_pickle
to_timedelta
tseries
unique
util
value_counts
wide_to_long
>>> 
>>> res=pd.Series(list('1234567'))
>>> res
0    1
1    2
2    3
3    4
4    5
5    6
6    7
dtype: object
>>> type(res)
<class 'pandas.core.series.Series'>
>>> res=pd.Series(list('1234567'),index=list('9876543'))
>>> res
9    1
8    2
7    3
6    4
5    5
4    6
3    7
dtype: object
>>> 
>>> res=pd.Series(tuple('1234567'),index=list('9876543'))
>>> res
9    1
8    2
7    3
6    4
5    5
4    6
3    7
dtype: object
>>> 
>>> movies=pd.Series(data=['Baghban','Spiderman','AEW','DDLJ','TMK','Dangal'], index=['*****','****','*****','**','***','***']
		 )
>>> movies
*****      Baghban
****     Spiderman
*****          AEW
**            DDLJ
***            TMK
***         Dangal
dtype: object
>>> 
>>> movies['******']
Traceback (most recent call last):
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 4736, in get_value
    return libindex.get_value_box(s, key)
  File "pandas/_libs/index.pyx", line 51, in pandas._libs.index.get_value_box
  File "pandas/_libs/index.pyx", line 47, in pandas._libs.index.get_value_at
  File "pandas/_libs/util.pxd", line 98, in pandas._libs.util.get_value_at
  File "pandas/_libs/util.pxd", line 83, in pandas._libs.util.validate_indexer
TypeError: 'str' object cannot be interpreted as an integer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    movies['******']
  File "C:\Python37\lib\site-packages\pandas\core\series.py", line 1071, in __getitem__
    result = self.index.get_value(self, key)
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 4744, in get_value
    raise e1
  File "C:\Python37\lib\site-packages\pandas\core\indexes\base.py", line 4730, in get_value
    return self._engine.get_value(s, k, tz=getattr(series.dtype, "tz", None))
  File "pandas/_libs/index.pyx", line 80, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 88, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 126, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 152, in pandas._libs.index.IndexEngine._get_loc_duplicates
  File "pandas/_libs/index.pyx", line 169, in pandas._libs.index.IndexEngine._maybe_get_bool_indexer
KeyError: '******'
>>> movies['*****']
*****    Baghban
*****        AEW
dtype: object
>>> movies['****']
'Spiderman'
>>> movies[['*****','****']]
*****      Baghban
*****          AEW
****     Spiderman
dtype: object
>>> 
>>> 
>>> res=pd.Series(data(1:10,2:20,3:30),index=[1,2,3,4])
SyntaxError: invalid syntax
>>> res=pd.Series(data{1:10,2:20,3:30},index=[1,2,3,4])
SyntaxError: invalid syntax
>>> res=pd.Series(data={1:10,2:20,3:30},index=[1,2,3,4])
>>> res
1    10.0
2    20.0
3    30.0
4     NaN
dtype: float64
>>> # We use dictationary in the above fucntion so we use {}
>>> res*10
1    100.0
2    200.0
3    300.0
4      NaN
dtype: float64
>>> 
>>> 
>>> dit=pd.DataFrame({"year":[2015,2016,2017,2018,2019],"students":[200,300,700,500,200],"faculty":[40,50,70,30,30],"placements":[150,200,350,100,20]})
>>> 
>>> dit
   year  students  faculty  placements
0  2015       200       40         150
1  2016       300       50         200
2  2017       700       70         350
3  2018       500       30         100
4  2019       200       30          20
>>> #converting dict into dataframe
>>> 
>>> dit['students&faculty']=dit['students']+dit['faculty']
>>> 
>>> dit
   year  students  faculty  placements  students&faculty
0  2015       200       40         150               240
1  2016       300       50         200               350
2  2017       700       70         350               770
3  2018       500       30         100               530
4  2019       200       30          20               230
>>> #Above is to add a column
>>> 
>>> del(dit['students&faculty'])
>>> dit
   year  students  faculty  placements
0  2015       200       40         150
1  2016       300       50         200
2  2017       700       70         350
3  2018       500       30         100
4  2019       200       30          20
>>> #Above is to delete a column
>>> 
>>> 
>>> dit[['year','placements']]
   year  placements
0  2015         150
1  2016         200
2  2017         350
3  2018         100
4  2019          20
>>> #Above for retrieving data from DataFrame
>>> 
>>> 
>>> dit['placements'].sum()
820
>>> dit['placements'].avg()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dit['placements'].avg()
  File "C:\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'avg'
>>> dit['placements'].max()
350
>>> dit['placements'].min()
20
>>> dit['students'].min()
200
>>> dit['students'].mean()
380.0
>>> dit['students'].mode()
0    200
dtype: int64
>>> dit['students'].medin()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dit['students'].medin()
  File "C:\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'medin'
>>> dit['students'].median()
300.0
>>> dit.describe()
              year    students    faculty  placements
count     5.000000    5.000000   5.000000    5.000000
mean   2017.000000  380.000000  44.000000  164.000000
std       1.581139  216.794834  16.733201  123.409886
min    2015.000000  200.000000  30.000000   20.000000
25%    2016.000000  200.000000  30.000000  100.000000
50%    2017.000000  300.000000  40.000000  150.000000
75%    2018.000000  500.000000  50.000000  200.000000
max    2019.000000  700.000000  70.000000  350.000000
>>> 
>>> #describe() function displays max, min, mean.....
>>> 
>>> employees=pd.read_csv('C:/Python37/Prog/files/Employee.csv')
>>> employees
     eid      fname     lname               email  ... salary comm    mid   did
0    100     Steven      King     sking@gmail.com  ...  24000  NaN    NaN  90.0
1    101      Neena   Kochhar  nkochhar@gmail.com  ...  17000  NaN  100.0  90.0
2    102        Lex   De Haan   ldehaan@gmail.com  ...  17000  NaN  100.0  90.0
3    103  Alexander    Hunold   ahunold@gmail.com  ...   9000  NaN  102.0  60.0
4    104      Bruce     Ernst    bernst@gmail.com  ...   6000  NaN  103.0  60.0
..   ...        ...       ...                 ...  ...    ...  ...    ...   ...
96   196      Alana     Walsh    awalsh@gmail.com  ...   3100  NaN  124.0  40.0
97   197      Kevin    Feeney   kfeeney@gmail.com  ...   3000  NaN  124.0  40.0
98   198     Donald  OConnell  doconnel@gmail.com  ...   2600  NaN  124.0  50.0
99   199    Douglas     Grant    dgrant@gmail.com  ...   2600  NaN  124.0  50.0
100  200   Jennifer    Whalen   jwhalen@gmail.com  ...   4400  NaN  101.0  10.0

[101 rows x 11 columns]
>>> 

>>> pd.set_option('display.max_rows',1000)
>>> pd.set_option('display.max_column',1000)
>>> pd.set_option('display.max_colwidth',1000)
>>> pd.set_option('display.max_width',1000)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    pd.set_option('display.max_width',1000)
  File "C:\Python37\lib\site-packages\pandas\_config\config.py", line 233, in __call__
    return self.__func__(*args, **kwds)
  File "C:\Python37\lib\site-packages\pandas\_config\config.py", line 123, in _set_option
    key = _get_single_key(k, silent)
  File "C:\Python37\lib\site-packages\pandas\_config\config.py", line 88, in _get_single_key
    raise OptionError("No such keys(s): {pat!r}".format(pat=pat))
pandas._config.config.OptionError: "No such keys(s): 'display.max_width'"
>>> pd.set_option('display.width',1000)
>>> employees
     eid        fname        lname               email               phone     hiredate       jobid  salary  comm    mid    did
0    100       Steven         King     sking@gmail.com        515.123.4567  17-06-1987      AD_PRES   24000   NaN    NaN   90.0
1    101        Neena      Kochhar  nkochhar@gmail.com        515.123.4568  21-09-1989        AD_VP   17000   NaN  100.0   90.0
2    102          Lex      De Haan   ldehaan@gmail.com        515.123.4569  13-01-1993        AD_VP   17000   NaN  100.0   90.0
3    103    Alexander       Hunold   ahunold@gmail.com        590.423.4567  03-01-1990      IT_PROG    9000   NaN  102.0   60.0
4    104        Bruce        Ernst    bernst@gmail.com        590.423.4568  21-05-1991      IT_PROG    6000   NaN  103.0   60.0
5    105        David       Austin   daustin@gmail.com        590.423.4569  25-06-1997      IT_PROG    4800   NaN  103.0   60.0
6    106        Valli    Pataballa  vpatabal@gmail.com        590.423.4560  05-02-1998      IT_PROG    4800   NaN  103.0   60.0
7    107        Diana      Lorentz  dlorentz@gmail.com        590.423.5567  07-02-1999      IT_PROG    4200   NaN  103.0   60.0
8    108        Nancy    Greenberg  ngreenbe@gmail.com        515.124.4569  17-08-1994       FI_MGR   12000   NaN  101.0  100.0
9    109       Daniel       Faviet   dfaviet@gmail.com        515.124.4169  16-08-1994   FI_ACCOUNT    9000   NaN  108.0  100.0
10   110         John         Chen     jchen@gmail.com        515.124.4269  28-09-1997   FI_ACCOUNT    8200   NaN  108.0  100.0
11   111       Ismael      Sciarra  isciarra@gmail.com        515.124.4369  30-09-1997   FI_ACCOUNT    7700   NaN  108.0  100.0
12   112  Jose Manuel        Urman   jmurman@gmail.com        515.124.4469  07-03-1998   FI_ACCOUNT    7800   NaN  108.0  100.0
13   113         Luis         Popp     lpopp@gmail.com        515.124.4567  07-12-1999   FI_ACCOUNT    6900   NaN  108.0  100.0
14   114          Den     Raphaely  drapheal@gmail.com        515.127.4561  07-12-1994       PU_MAN   11000   NaN  100.0   30.0
15   115    Alexander         Khoo   akhoo@gmail.co.in        515.127.4562  18-05-1995     PU_CLERK    3100   NaN  114.0   30.0
16   116       Shelli        Baida    sbaida@gmail.com        515.127.4563  24-12-1997     PU_CLERK    2900   NaN  114.0   30.0
17   117        Sigal       Tobias   stobias@gmail.com        515.127.4564  24-07-1997     PU_CLERK    2800   NaN  114.0   30.0
18   118          Guy       Himuro   ghimuro@gmail.com        515.127.4565  15-11-1998     PU_CLERK    2600   NaN  114.0   30.0
19   119        Karen   Colmenares  kcolmena@gmail.com        515.127.4566  10-08-1999     PU_CLERK    2500   NaN  114.0   30.0
20   120      Matthew        Weiss    mweiss@gmail.com        650.123.1234  18-07-1996       ST_MAN    8000   NaN  100.0   50.0
21   121         Adam        Fripp    afripp@gmail.com        650.123.2234  10-04-1997       ST_MAN    8200   NaN  100.0   50.0
22   122        Payam     Kaufling  pkauflin@gmail.com        650.123.3234  01-05-1995       ST_MAN    7900   NaN  100.0   50.0
23   123       Shanta      Vollman  svollman@gmail.com        650.123.4234  10-10-1997       ST_MAN    6500   NaN  100.0   50.0
24   124        Kevin      Mourgos  kmourgos@gmail.com        650.123.5234  16-11-1999       ST_MAN    5800   NaN  100.0   50.0
25   125        Julia        Nayer    jnayer@gmail.com        650.124.1214  16-07-1997     ST_CLERK    3200   NaN  120.0   50.0
26   126        Irene  Mikkilineni  imikkili@gmail.com        650.124.1224  28-09-1998     ST_CLERK    2700   NaN  120.0   50.0
27   127        James       Landry   jlandry@gmail.com        650.124.1334  14-01-1999     ST_CLERK    2400   NaN  120.0   50.0
28   128       Steven       Markle   smarkle@gmail.com        650.124.1434  08-03-2000     ST_CLERK    2200   NaN  120.0   50.0
29   129        Laura       Bissot   lbissot@gmail.com        650.124.5234  20-08-1997     ST_CLERK    3300   NaN  121.0   50.0
30   130        Mozhe     Atkinson  matkinso@gmail.com        650.124.6234  30-10-1997     ST_CLERK    2800   NaN  121.0   50.0
31   131        James       Marlow   jamrlow@gmail.com        650.124.7234  16-02-1997     ST_CLERK    2500   NaN  121.0   50.0
32   132           TJ        Olson   tjolson@gmail.com        650.124.8234  10-04-1999     ST_CLERK    2100   NaN  121.0   50.0
33   133        Jason       Mallin   jmallin@gmail.com        650.127.1934  14-06-1996     ST_CLERK    3300   NaN  122.0   50.0
34   134      Michael       Rogers   mrogers@gmail.com        650.127.1834  26-08-1998     ST_CLERK    2900   NaN  122.0   50.0
35   135           Ki          Gee      kgee@gmail.com        650.127.1734  12-12-1999     ST_CLERK    2400   NaN  122.0   50.0
36   136        Hazel   Philtanker  hphiltan@gmail.com        650.127.1634  06-02-2000     ST_CLERK    2200   NaN  122.0   50.0
37   137       Renske       Ladwig   rladwig@gmail.com        650.121.1234  14-07-1995     ST_CLERK    3600   NaN  123.0   50.0
38   138      Stephen       Stiles   sstiles@gmail.com        650.121.2034  26-10-1997     ST_CLERK    3200   NaN  123.0   50.0
39   139         John          Seo      jseo@gmail.com        650.121.2019  12-02-1998     ST_CLERK    2700   NaN  123.0   50.0
40   140       Joshua        Patel    jpatel@gmail.com        650.121.1834  06-04-1998     ST_CLERK    2500   NaN  123.0   20.0
41   141       Trenna         Rajs     trajs@gmail.com        650.121.8009  17-10-1995     ST_CLERK    3500   NaN  124.0   20.0
42   142       Curtis       Davies   cdavies@gmail.com        650.121.2994  29-01-1997     ST_CLERK    3100   NaN  124.0   50.0
43   143      Randall        Matos    rmatos@gmail.com        650.121.2874  15-03-1998     ST_CLERK    2600   NaN  124.0   50.0
44   144        Peter       Vargas   pvargas@gmail.com        650.121.2004  09-07-1998     ST_CLERK    2500   NaN  124.0   50.0
45   145         John      Russell   jrussel@gmail.com  011.44.1344.429268  01-10-1996       SA_MAN   14000  0.40  100.0   80.0
46   146        Karen     Partners  kpartner@gmail.com  011.44.1344.467268  05-01-1997       SA_MAN   13500  0.30  100.0   80.0
47   147      Alberto    Errazuriz  aerrazur@gmail.com  011.44.1344.429278  10-03-1997       SA_MAN   12000  0.30  100.0   80.0
48   148       Gerald    Cambrault  gcambrau@gmail.com  011.44.1344.619268  15-10-1999       SA_MAN   11000  0.30  100.0   80.0
49   149        Eleni      Zlotkey  ezlotkey@gmail.com  011.44.1344.429018  29-01-2000       SA_MAN   10500  0.20  100.0   80.0
50   150        Peter       Tucker   ptucker@gmail.com  011.44.1344.129268  30-01-1997       SA_REP   10000  0.30  145.0   80.0
51   151        David    Bernstein  dbernste@gmail.com  011.44.1344.345268  24-03-1997       SA_REP    9500  0.25  145.0   80.0
52   152        Peter         Hall     phall@gmail.com  011.44.1344.478968  20-08-1997       SA_REP    9000  0.25  145.0   80.0
53   153  Christopher        Olsen    colsen@gmail.com  011.44.1344.498718  30-03-1998       SA_REP    8000  0.20  145.0   80.0
54   154      Nanette    Cambrault  ncambrau@gmail.com  011.44.1344.987668  09-12-1998       SA_REP    7500  0.20  145.0   80.0
55   155       Oliver      Tuvault  otuvault@gmail.com  011.44.1344.486508  23-11-1999       SA_REP    7000  0.15  145.0   80.0
56   156      Janette         King     jking@gmail.com  011.44.1345.429268  30-01-1996       SA_REP   10000  0.35  146.0   80.0
57   157      Patrick        Sully    psully@gmail.com  011.44.1345.929268  04-03-1996       SA_REP    9500  0.35  146.0   80.0
58   158        Allan       McEwen   amcewen@gmail.com  011.44.1345.829268  01-08-1996       SA_REP    9000  0.35  146.0   80.0
59   159      Lindsey        Smith    lsmith@gmail.com  011.44.1345.729268  10-03-1997       SA_REP    8000  0.30  146.0   80.0
60   160       Louise        Doran    ldoran@gmail.com  011.44.1345.629268  15-12-1997       SA_REP    7500  0.30  146.0   80.0
61   161       Sarath       Sewall   ssewall@gmail.com  011.44.1345.529268  03-11-1998       SA_REP    7000  0.25  146.0   80.0
62   162        Clara      Vishney  cvishney@gmail.com  011.44.1346.129268  11-11-1997       SA_REP   10500  0.25  147.0   80.0
63   163     Danielle       Greene   dgreene@gmail.com  011.44.1346.229268  19-03-1999       SA_REP    9500  0.15  147.0   80.0
64   164       Mattea      Marvins  mmarvins@gmail.com  011.44.1346.329268  24-01-2000       SA_REP    7200  0.10  147.0   80.0
65   165        David          Lee      dlee@gmail.com  011.44.1346.529268  23-02-2000       SA_REP    6800  0.10  147.0   80.0
66   166       Sundar         Ande     sande@gmail.com  011.44.1346.629268  24-03-2000       SA_REP    6400  0.10  147.0   80.0
67   167         Amit        Banda    abanda@gmail.com  011.44.1346.729268  21-04-2000       SA_REP    6200  0.10  147.0   80.0
68   168         Lisa         Ozer     lozer@gmail.com  011.44.1343.929268  11-03-1997       SA_REP   11500  0.25  148.0   80.0
69   169     Harrison        Bloom    hbloom@gmail.com  011.44.1343.829268  23-03-1998       SA_REP   10000  0.20  148.0   80.0
70   170       Tayler          Fox      tfox@gmail.com  011.44.1343.729268  24-01-1998       SA_REP    9600  0.20  148.0   80.0
71   171      William        Smith    wsmith@gmail.com  011.44.1343.629268  23-02-1999       SA_REP    7400  0.15  148.0   80.0
72   172    Elizabeth        Bates    ebates@gmail.com  011.44.1343.529268  24-03-1999       SA_REP    7300  0.15  148.0   80.0
73   173      Sundita        Kumar    skumar@gmail.com  011.44.1343.329268  21-04-2000       SA_REP    6100  0.10  148.0   80.0
74   174        Ellen         Abel     eabel@gmail.com  011.44.1644.429267  11-05-1996       SA_REP   11000  0.30  149.0   80.0
75   175       Alyssa       Hutton   ahutton@gmail.com  011.44.1644.429266  19-03-1997       SA_REP    8800  0.25  149.0   80.0
76   176     Jonathon       Taylor   jtaylor@gmail.com  011.44.1644.429265  24-03-1998       SA_REP    8600  0.20  149.0   80.0
77   177         Jack   Livingston  jlivings@gmail.com  011.44.1644.429264  23-04-1998       SA_REP    8400  0.20  149.0   80.0
78   178    Kimberely        Grant    kgrant@gmail.com  011.44.1644.429263  24-05-1999       SA_REP    7000  0.15  149.0    NaN
79   179      Charles      Johnson  cjohnson@gmail.com  011.44.1644.429262  04-01-2000       SA_REP    6200  0.10  149.0   80.0
80   180      Winston       Taylor   wtaylor@gmail.com        650.507.9876  24-01-1998     SH_CLERK    3200   NaN  120.0   50.0
81   181         Jean       Fleaur   jfleaur@gmail.com        650.507.9877  23-02-1998     SH_CLERK    3100   NaN  120.0   50.0
82   182       Martha     Sullivan  msulliva@gmail.com        650.507.9878  21-06-1999     SH_CLERK    2500   NaN  120.0   50.0
83   183       Girard        Geoni    ggeoni@gmail.com        650.507.9879  03-02-2000     SH_CLERK    2800   NaN  120.0   50.0
84   184      Nandita     Sarchand  nsarchan@gmail.com        650.509.1876  27-01-1996     SH_CLERK    4200   NaN  121.0   50.0
85   185       Alexis         Bull     abull@gmail.com        650.509.2876  20-02-1997     SH_CLERK    4100   NaN  121.0   50.0
86   186        Julia    Dellinger  jdelling@gmail.com        650.509.3876  24-06-1998     SH_CLERK    3400   NaN  121.0   50.0
87   187      Anthony       Cabrio   acabrio@gmail.com        650.509.4876  07-02-1999     SH_CLERK    3000   NaN  121.0   50.0
88   188        Kelly        Chung    kchung@gmail.com        650.505.1876  14-06-1997     SH_CLERK    3800   NaN  122.0   50.0
89   189     Jennifer        Dilly    jdilly@gmail.com        650.505.2876  13-08-1997     SH_CLERK    3600   NaN  122.0   50.0
90   190      Timothy        Gates    tgates@gmail.com        650.505.3876  11-07-1998     SH_CLERK    2900   NaN  122.0   50.0
91   191      Randall      Perkins  rperkins@gmail.com        650.505.4876  19-12-1999     SH_CLERK    2500   NaN  122.0   50.0
92   192        Sarah         Bell     sbell@gmail.com        650.501.1876  04-02-1996     SH_CLERK    4000   NaN  123.0   50.0
93   193      Britney      Everett  beverett@gmail.com        650.501.2876  03-03-1997     SH_CLERK    3900   NaN  123.0   50.0
94   194       Samuel       McCain   smccain@gmail.com        650.501.3876  01-07-1998     SH_CLERK    3200   NaN  123.0   40.0
95   195        Vance        Jones    vjones@gmail.com        650.501.4876  17-03-1999     SH_CLERK    2800   NaN  123.0   40.0
96   196        Alana        Walsh    awalsh@gmail.com        650.507.9811  24-04-1998     SH_CLERK    3100   NaN  124.0   40.0
97   197        Kevin       Feeney   kfeeney@gmail.com        650.507.9822  23-05-1998     SH_CLERK    3000   NaN  124.0   40.0
98   198       Donald     OConnell  doconnel@gmail.com        650.507.9833  21-06-1999     SH_CLERK    2600   NaN  124.0   50.0
99   199      Douglas        Grant    dgrant@gmail.com        650.507.9844  13-01-2000     SH_CLERK    2600   NaN  124.0   50.0
100  200     Jennifer       Whalen   jwhalen@gmail.com        515.123.4444  17-09-1987      AD_ASST    4400   NaN  101.0   10.0
>>> 
>>> 
>>> employees['eid']

>>> employees[['eid','fname','lname']]
     eid        fname        lname
0    100       Steven         King
1    101        Neena      Kochhar
2    102          Lex      De Haan
3    103    Alexander       Hunold
4    104        Bruce        Ernst
5    105        David       Austin
6    106        Valli    Pataballa
7    107        Diana      Lorentz
8    108        Nancy    Greenberg
9    109       Daniel       Faviet
10   110         John         Chen
11   111       Ismael      Sciarra
12   112  Jose Manuel        Urman
13   113         Luis         Popp
14   114          Den     Raphaely
15   115    Alexander         Khoo
16   116       Shelli        Baida
17   117        Sigal       Tobias
18   118          Guy       Himuro
19   119        Karen   Colmenares
20   120      Matthew        Weiss
21   121         Adam        Fripp
22   122        Payam     Kaufling
23   123       Shanta      Vollman
24   124        Kevin      Mourgos
25   125        Julia        Nayer
26   126        Irene  Mikkilineni
27   127        James       Landry
28   128       Steven       Markle
29   129        Laura       Bissot
30   130        Mozhe     Atkinson
31   131        James       Marlow
32   132           TJ        Olson
33   133        Jason       Mallin
34   134      Michael       Rogers
35   135           Ki          Gee
36   136        Hazel   Philtanker
37   137       Renske       Ladwig
38   138      Stephen       Stiles
39   139         John          Seo
40   140       Joshua        Patel
41   141       Trenna         Rajs
42   142       Curtis       Davies
43   143      Randall        Matos
44   144        Peter       Vargas
45   145         John      Russell
46   146        Karen     Partners
47   147      Alberto    Errazuriz
48   148       Gerald    Cambrault
49   149        Eleni      Zlotkey
50   150        Peter       Tucker
51   151        David    Bernstein
52   152        Peter         Hall
53   153  Christopher        Olsen
54   154      Nanette    Cambrault
55   155       Oliver      Tuvault
56   156      Janette         King
57   157      Patrick        Sully
58   158        Allan       McEwen
59   159      Lindsey        Smith
60   160       Louise        Doran
61   161       Sarath       Sewall
62   162        Clara      Vishney
63   163     Danielle       Greene
64   164       Mattea      Marvins
65   165        David          Lee
66   166       Sundar         Ande
67   167         Amit        Banda
68   168         Lisa         Ozer
69   169     Harrison        Bloom
70   170       Tayler          Fox
71   171      William        Smith
72   172    Elizabeth        Bates
73   173      Sundita        Kumar
74   174        Ellen         Abel
75   175       Alyssa       Hutton
76   176     Jonathon       Taylor
77   177         Jack   Livingston
78   178    Kimberely        Grant
79   179      Charles      Johnson
80   180      Winston       Taylor
81   181         Jean       Fleaur
82   182       Martha     Sullivan
83   183       Girard        Geoni
84   184      Nandita     Sarchand
85   185       Alexis         Bull
86   186        Julia    Dellinger
87   187      Anthony       Cabrio
88   188        Kelly        Chung
89   189     Jennifer        Dilly
90   190      Timothy        Gates
91   191      Randall      Perkins
92   192        Sarah         Bell
93   193      Britney      Everett
94   194       Samuel       McCain
95   195        Vance        Jones
96   196        Alana        Walsh
97   197        Kevin       Feeney
98   198       Donald     OConnell
99   199      Douglas        Grant
100  200     Jennifer       Whalen
>>> 
>>> 
>>> length(employees)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    length(employees)
NameError: name 'length' is not defined
>>> len(employees)
101
>>> employees.column
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    employees.column
  File "C:\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'column'
>>> employees.columns
Index(['eid', 'fname', 'lname', 'email', 'phone', 'hiredate', 'jobid', 'salary', 'comm', 'mid', 'did'], dtype='object')
>>> 
>>> employees.dtype
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    employees.dtype
  File "C:\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'dtype'
>>> employees.dstype
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    employees.dstype
  File "C:\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'dstype'
>>> employees.dtypes
eid           int64
fname        object
lname        object
email        object
phone        object
hiredate     object
jobid        object
salary        int64
comm        float64
mid         float64
did         float64
dtype: object
>>> 
>>> #Another method for retrieving data
>>> employees.eid

>>> #for Specific record
>>> 
>>> employees.head()
   eid      fname    lname               email         phone     hiredate    jobid  salary  comm    mid   did
0  100     Steven     King     sking@gmail.com  515.123.4567  17-06-1987   AD_PRES   24000   NaN    NaN  90.0
1  101      Neena  Kochhar  nkochhar@gmail.com  515.123.4568  21-09-1989     AD_VP   17000   NaN  100.0  90.0
2  102        Lex  De Haan   ldehaan@gmail.com  515.123.4569  13-01-1993     AD_VP   17000   NaN  100.0  90.0
3  103  Alexander   Hunold   ahunold@gmail.com  590.423.4567  03-01-1990   IT_PROG    9000   NaN  102.0  60.0
4  104      Bruce    Ernst    bernst@gmail.com  590.423.4568  21-05-1991   IT_PROG    6000   NaN  103.0  60.0
>>> #bY default value is 5 so displaying 5 records
>>> 
>>> # for getting last record we use tail()
>>> employee.tail()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    employee.tail()
NameError: name 'employee' is not defined
>>> employees.tail()
     eid     fname     lname               email         phone     hiredate     jobid  salary  comm    mid   did
96   196     Alana     Walsh    awalsh@gmail.com  650.507.9811  24-04-1998   SH_CLERK    3100   NaN  124.0  40.0
97   197     Kevin    Feeney   kfeeney@gmail.com  650.507.9822  23-05-1998   SH_CLERK    3000   NaN  124.0  40.0
98   198    Donald  OConnell  doconnel@gmail.com  650.507.9833  21-06-1999   SH_CLERK    2600   NaN  124.0  50.0
99   199   Douglas     Grant    dgrant@gmail.com  650.507.9844  13-01-2000   SH_CLERK    2600   NaN  124.0  50.0
100  200  Jennifer    Whalen   jwhalen@gmail.com  515.123.4444  17-09-1987    AD_ASST    4400   NaN  101.0  10.0
>>> 

>>> 
>>> 
>>> #for accesing a particular record
>>> 
>>> employees.iloc[5]
eid                       105
fname                   David
lname                  Austin
email       daustin@gmail.com
phone            590.423.4569
hiredate          25-06-1997 
jobid                 IT_PROG
salary                   4800
comm                      NaN
mid                       103
did                        60
Name: 5, dtype: object
>>> employees.iloc[5:10]
   eid   fname      lname               email         phone     hiredate       jobid  salary  comm    mid    did
5  105   David     Austin   daustin@gmail.com  590.423.4569  25-06-1997      IT_PROG    4800   NaN  103.0   60.0
6  106   Valli  Pataballa  vpatabal@gmail.com  590.423.4560  05-02-1998      IT_PROG    4800   NaN  103.0   60.0
7  107   Diana    Lorentz  dlorentz@gmail.com  590.423.5567  07-02-1999      IT_PROG    4200   NaN  103.0   60.0
8  108   Nancy  Greenberg  ngreenbe@gmail.com  515.124.4569  17-08-1994       FI_MGR   12000   NaN  101.0  100.0
9  109  Daniel     Faviet   dfaviet@gmail.com  515.124.4169  16-08-1994   FI_ACCOUNT    9000   NaN  108.0  100.0
>>> #It's like slicing
>>> 
>>> employees[employees.eid==100]
   eid   fname lname            email         phone     hiredate    jobid  salary  comm  mid   did
0  100  Steven  King  sking@gmail.com  515.123.4567  17-06-1987   AD_PRES   24000   NaN  NaN  90.0
>>> employees[employees.salary<3000]
    eid    fname        lname               email         phone     hiredate     jobid  salary  comm    mid   did
16  116   Shelli        Baida    sbaida@gmail.com  515.127.4563  24-12-1997   PU_CLERK    2900   NaN  114.0  30.0
17  117    Sigal       Tobias   stobias@gmail.com  515.127.4564  24-07-1997   PU_CLERK    2800   NaN  114.0  30.0
18  118      Guy       Himuro   ghimuro@gmail.com  515.127.4565  15-11-1998   PU_CLERK    2600   NaN  114.0  30.0
19  119    Karen   Colmenares  kcolmena@gmail.com  515.127.4566  10-08-1999   PU_CLERK    2500   NaN  114.0  30.0
26  126    Irene  Mikkilineni  imikkili@gmail.com  650.124.1224  28-09-1998   ST_CLERK    2700   NaN  120.0  50.0
27  127    James       Landry   jlandry@gmail.com  650.124.1334  14-01-1999   ST_CLERK    2400   NaN  120.0  50.0
28  128   Steven       Markle   smarkle@gmail.com  650.124.1434  08-03-2000   ST_CLERK    2200   NaN  120.0  50.0
30  130    Mozhe     Atkinson  matkinso@gmail.com  650.124.6234  30-10-1997   ST_CLERK    2800   NaN  121.0  50.0
31  131    James       Marlow   jamrlow@gmail.com  650.124.7234  16-02-1997   ST_CLERK    2500   NaN  121.0  50.0
32  132       TJ        Olson   tjolson@gmail.com  650.124.8234  10-04-1999   ST_CLERK    2100   NaN  121.0  50.0
34  134  Michael       Rogers   mrogers@gmail.com  650.127.1834  26-08-1998   ST_CLERK    2900   NaN  122.0  50.0
35  135       Ki          Gee      kgee@gmail.com  650.127.1734  12-12-1999   ST_CLERK    2400   NaN  122.0  50.0
36  136    Hazel   Philtanker  hphiltan@gmail.com  650.127.1634  06-02-2000   ST_CLERK    2200   NaN  122.0  50.0
39  139     John          Seo      jseo@gmail.com  650.121.2019  12-02-1998   ST_CLERK    2700   NaN  123.0  50.0
40  140   Joshua        Patel    jpatel@gmail.com  650.121.1834  06-04-1998   ST_CLERK    2500   NaN  123.0  20.0
43  143  Randall        Matos    rmatos@gmail.com  650.121.2874  15-03-1998   ST_CLERK    2600   NaN  124.0  50.0
44  144    Peter       Vargas   pvargas@gmail.com  650.121.2004  09-07-1998   ST_CLERK    2500   NaN  124.0  50.0
82  182   Martha     Sullivan  msulliva@gmail.com  650.507.9878  21-06-1999   SH_CLERK    2500   NaN  120.0  50.0
83  183   Girard        Geoni    ggeoni@gmail.com  650.507.9879  03-02-2000   SH_CLERK    2800   NaN  120.0  50.0
90  190  Timothy        Gates    tgates@gmail.com  650.505.3876  11-07-1998   SH_CLERK    2900   NaN  122.0  50.0
91  191  Randall      Perkins  rperkins@gmail.com  650.505.4876  19-12-1999   SH_CLERK    2500   NaN  122.0  50.0
95  195    Vance        Jones    vjones@gmail.com  650.501.4876  17-03-1999   SH_CLERK    2800   NaN  123.0  40.0
98  198   Donald     OConnell  doconnel@gmail.com  650.507.9833  21-06-1999   SH_CLERK    2600   NaN  124.0  50.0
99  199  Douglas        Grant    dgrant@gmail.com  650.507.9844  13-01-2000   SH_CLERK    2600   NaN  124.0  50.0
>>> #To get only salary coloumn
>>> employees[employees.salary<3000][['lname','salary']]
          lname  salary
16        Baida    2900
17       Tobias    2800
18       Himuro    2600
19   Colmenares    2500
26  Mikkilineni    2700
27       Landry    2400
28       Markle    2200
30     Atkinson    2800
31       Marlow    2500
32        Olson    2100
34       Rogers    2900
35          Gee    2400
36   Philtanker    2200
39          Seo    2700
40        Patel    2500
43        Matos    2600
44       Vargas    2500
82     Sullivan    2500
83        Geoni    2800
90        Gates    2900
91      Perkins    2500
95        Jones    2800
98     OConnell    2600
99        Grant    2600
>>> #P.s. above we got the lname column as well. Don't get confused regarding that.
>>> employees[employees.salary<3000][['lname','salary','did']]
          lname  salary   did
16        Baida    2900  30.0
17       Tobias    2800  30.0
18       Himuro    2600  30.0
19   Colmenares    2500  30.0
26  Mikkilineni    2700  50.0
27       Landry    2400  50.0
28       Markle    2200  50.0
30     Atkinson    2800  50.0
31       Marlow    2500  50.0
32        Olson    2100  50.0
34       Rogers    2900  50.0
35          Gee    2400  50.0
36   Philtanker    2200  50.0
39          Seo    2700  50.0
40        Patel    2500  20.0
43        Matos    2600  50.0
44       Vargas    2500  50.0
82     Sullivan    2500  50.0
83        Geoni    2800  50.0
90        Gates    2900  50.0
91      Perkins    2500  50.0
95        Jones    2800  40.0
98     OConnell    2600  50.0
99        Grant    2600  50.0
>>> employees[[employees.salary<3000]|[employees['did']==10]][['lname','salary','did']]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    employees[[employees.salary<3000]|[employees['did']==10]][['lname','salary','did']]
TypeError: unsupported operand type(s) for |: 'list' and 'list'
>>> employees[(employees.salary<3000)|(employees['did']==10)][['lname','salary','did']]
           lname  salary   did
16         Baida    2900  30.0
17        Tobias    2800  30.0
18        Himuro    2600  30.0
19    Colmenares    2500  30.0
26   Mikkilineni    2700  50.0
27        Landry    2400  50.0
28        Markle    2200  50.0
30      Atkinson    2800  50.0
31        Marlow    2500  50.0
32         Olson    2100  50.0
34        Rogers    2900  50.0
35           Gee    2400  50.0
36    Philtanker    2200  50.0
39           Seo    2700  50.0
40         Patel    2500  20.0
43         Matos    2600  50.0
44        Vargas    2500  50.0
82      Sullivan    2500  50.0
83         Geoni    2800  50.0
90         Gates    2900  50.0
91       Perkins    2500  50.0
95         Jones    2800  40.0
98      OConnell    2600  50.0
99         Grant    2600  50.0
100       Whalen    4400  10.0
>>> #Above For applying multiple conditions
>>> employees[(employees.salary<3000)&(employees['did']==30)][['lname','salary','did']]
         lname  salary   did
16       Baida    2900  30.0
17      Tobias    2800  30.0
18      Himuro    2600  30.0
19  Colmenares    2500  30.0
>>> 
