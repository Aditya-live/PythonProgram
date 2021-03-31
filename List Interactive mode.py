Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst=list()
>>> lst
[]
>>> type(lst)
<class 'list'>
>>> lst=list{"james"}
SyntaxError: invalid syntax
>>> lst=list("james")
>>> lst
['j', 'a', 'm', 'e', 's']
>>> lst=list(10)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    lst=list(10)
TypeError: 'int' object is not iterable
>>> lst=list("10")
>>> lst
['1', '0']
>>> lst=list("a")
>>> lst
['a']
>>> lst[10,20,30,40,50]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lst[10,20,30,40,50]
TypeError: list indices must be integers or slices, not tuple
>>> lst=[10,20,30,40,50]
>>> lst[0]
10
>>> lst[-1]
50
>>> lst[::-1]
[50, 40, 30, 20, 10]
>>> lst=["james",10,12.34,12+5j]
>>> for i in lst:
	print(type(i))

	
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
>>> 
>>> 
>>> lst=['a','b','c']
>>> id(lst)
2406290336456
>>> lst.append('d')
>>> lst
['a', 'b', 'c', 'd']
>>> id(lst)
2406290336456
>>> del(lst[3])
\
>>> lst
['a', 'b', 'c']
>>> lst1=[10,20,30]
>>> lst2=lst2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lst2=lst2
NameError: name 'lst2' is not defined
>>> lst2=lst1
>>> lst2.append(100)
>>> lst2
[10, 20, 30, 100]
>>> lst1
[10, 20, 30, 100]
>>> lst[[10,20,30],[40,50,60],[70,80,90]]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    lst[[10,20,30],[40,50,60],[70,80,90]]
TypeError: list indices must be integers or slices, not tuple
>>> lst=[[10,20,30],[40,50,60],[70,80,90]]
>>> for row in lst:
	print(row)

	
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
>>> print(lst)
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
>>> for row in lst:
	for j in lst:
		print(j)

		
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
>>> for row in lst:
	for j in i:
		print(j)

		
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    for j in i:
TypeError: 'complex' object is not iterable
>>> for row in lst:
	for j in i:
		print(j)

		
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    for j in i:
TypeError: 'complex' object is not iterable
>>> for row in lst:
	for j in i:
		print(j,end=" ")
	print()

	
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    for j in i:
TypeError: 'complex' object is not iterable
>>> for row in lst:
	for j in col:
		print(col,end=" ")
	print()

	
Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    for j in col:
NameError: name 'col' is not defined
>>> lst
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
>>> for row in lst:
	for col in row:
		print(col,end=" ")
	print()

	
10 20 30 
40 50 60 
70 80 90 
>>> 
for row in lst:
	for j in col:
		print(col,end=" ")
	print()

	
Traceback (most recent call last):
  File "<pyshell#61>", line 3, in <module>
    for j in col:
TypeError: 'int' object is not iterable
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lst=[10,20,[30,40,50],60,[70,80,90]]
>>> lst
[10, 20, [30, 40, 50], 60, [70, 80, 90]]
>>> for i in lst:
	for j in i:
		print(j)
	print()

	
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    for j in i:
TypeError: 'int' object is not iterable
>>> for i in lst:
	if type(list[i])==list:
		for j in i:
			print(j,end=" ")
	else:
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#81>", line 2, in <module>
    if type(list[i])==list:
TypeError: 'type' object is not subscriptable
>>> j
[70, 80, 90]
>>> for i in lst:
	if type(i)==list:
		for j in i:
			print(j,end=" ")
	else:
		print(i)

		
10
20
30 40 50 60
70 80 90 
>>> for i in lst:
	if type(i)==list:
		for j in i:
			print(j,end=" ")
		print()
	else:
		print(i)

		
10
20
30 40 50 
60
70 80 90 
>>> import collections
>>> lst
[10, 20, [30, 40, 50], 60, [70, 80, 90]]
>>> for i in lst:
	if isinstance(i,collections.Iterable):
		for j in i:
			print(j,end=" ")
		print()
	else:
		print(i)

		

Warning (from warnings module):
  File "__main__", line 2
DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
10
20
30 40 50 
60
70 80 90 
>>> import warnings
>>> warnings.filterwarnings(action="ignore")
>>> lst = [10,20,30,40,50]
>>> lst.append(60)
>>> lst
[10, 20, 30, 40, 50, 60]
>>> lst.clear
<built-in method clear of list object at 0x000002304213C4C8>
>>> lst
[10, 20, 30, 40, 50, 60]
>>> lst.clear()
>>> lst
[]
>>> lst=[10,20,30,40,50]
>>> lst2=lst
>>> lst2[0]=100
>>> lst3=lst.copy
>>> lst3
<built-in method copy of list object at 0x0000023042140A88>
>>> lst
[100, 20, 30, 40, 50]
>>> lst3[0]=10000
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    lst3[0]=10000
TypeError: 'builtin_function_or_method' object does not support item assignment
>>> lst3=lst.copy()
>>> lst3[0]=1000
>>> lst3
[1000, 20, 30, 40, 50]
>>> lst
[100, 20, 30, 40, 50]
>>> lst.count(40)
1
>>> lst=[20,30,30,[20,30]]
>>> lst.count(20)
1
>>> lst
[20, 30, 30, [20, 30]]
>>> lst.extend(lst2)
>>> lst
[20, 30, 30, [20, 30], 100, 20, 30, 40, 50]
>>> lst
[20, 30, 30, [20, 30], 100, 20, 30, 40, 50]
>>> lst.index(30)
1
>>> lst.insert(2,1000)
>>> lst
[20, 30, 1000, 30, [20, 30], 100, 20, 30, 40, 50]
>>> lst.pop()
50
>>> lst.pop(2)
1000
>>> lst
[20, 30, 30, [20, 30], 100, 20, 30, 40]
>>> lst.remove(30)
>>> lst
[20, 30, [20, 30], 100, 20, 30, 40]
>>> lst.reverse()
>>> lst
[40, 30, 20, 100, [20, 30], 30, 20]
>>> lst[-1]
20
>>> lst.sort()
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    lst.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> lst=[10,20,40,30]
>>> lst.reverse()
>>> lst
[30, 40, 20, 10]
>>> lst.sort()
>>> lst
[10, 20, 30, 40]
>>> lst.sort(reverse=True)
>>> lst
[40, 30, 20, 10]
>>> lst=["james","aditya", "jen","paul"]
>>> for in lst:
	
SyntaxError: invalid syntax
>>> 
=================== RESTART: C:/Python37/Prog/lessthan5.py ===================
<built-in method upper of str object at 0x00000259EAAC7688>
<built-in method upper of str object at 0x00000259EAAC76C0>
<built-in method lower of str object at 0x00000259EAAC7650>
<built-in method lower of str object at 0x00000259EAAC76F8>
>>> 
=================== RESTART: C:/Python37/Prog/lessthan5.py ===================
jen
paul
['JAMES', 'ADITYA']
>>> 
=================== RESTART: C:/Python37/Prog/lessthan5.py ===================
['JAMES', 'ADITYA']
>>> 
>>> 
=================== RESTART: C:/Python37/Prog/lessthan5.py ===================
Traceback (most recent call last):
  File "C:/Python37/Prog/lessthan5.py", line 10, in <module>
    print([nm for nm in names if len(nm>=5)])
NameError: name 'names' is not defined
>>> 
=================== RESTART: C:/Python37/Prog/lessthan5.py ===================
Traceback (most recent call last):
  File "C:/Python37/Prog/lessthan5.py", line 10, in <module>
    print([nm for nm in name if len(nm>=5)])
  File "C:/Python37/Prog/lessthan5.py", line 10, in <listcomp>
    print([nm for nm in name if len(nm>=5)])
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 
=================== RESTART: C:/Python37/Prog/lessthan5.py ===================
['james', 'aditya']
>>> 
=================== RESTART: C:/Python37/Prog/lessthan5.py ===================
['JAMES', 'ADITYA']
>>> a=10
>>> b=20
>>> print(a) if(a>b) else print(b)
20
>>> 
>>> 
>>> print(i**3) for i in range(1,10)
SyntaxError: invalid syntax
>>> print([i**3 for i in range(1,10)])
[1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> print([i**3 for i in range(1,11)])
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> 

>>> 
>>> print([[i,i**2,i**3] for i in range(1,11)])
