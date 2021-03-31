Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=()
>>> x.count
<built-in method count of tuple object at 0x00000210A8690048>
>>> x.count()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.count()
TypeError: count() takes exactly one argument (0 given)
>>> x=('java',23,3.6,34)
>>> print(x)
('java', 23, 3.6, 34)
>>> len(x)
4
>>> x=(1,2,3)
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=(1,2,3)
>>> (a,b,c) =x
>>> a
1
>>> b
2
>>> c
3
>>> (a,b,c,d) =x
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    (a,b,c,d) =x
ValueError: not enough values to unpack (expected 4, got 3)
>>> (a,b) =x
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    (a,b) =x
ValueError: too many values to unpack (expected 2)
>>> x
(1, 2, 3)
>>> print(enumerate(x))
<enumerate object at 0x00000210AAE50948>
>>> print(tuple(enumerate(x)))
((0, 1), (1, 2), (2, 3))
>>> 
>>> sorted(range(1,11,2),reverse=True)
[9, 7, 5, 3, 1]
>>> x=(1,23,4.5,12)
>>> x=(1,23,4.5,12)
>>> for cnt,val in enumerate(x):
	print cnt,val
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(cnt,val)?
>>> 
>>> for cnt,val in enumerate(x):
	print(cnt,val)

	
0 1
1 23
2 4.5
3 12
>>> lst1=[1,2,3]
>>> lst2=[3,4,1]
>>> for cnt,val in enumerate(lst2):
	lst1.insert(2+cnt,val)

	
>>> print(lst1)
[1, 2, 3, 4, 1, 3]
>>> lst1=[1,2,3]
>>> lst2=[1,3,5,7]
>>> for cnt,val in enumerate(lst2):
	lst1.insert(2+cnt,val)

	
>>> print(lst1)
[1, 2, 1, 3, 5, 7, 3]
>>> x={}
>>> x
{}
>>> x={1:"java",2:"python",3:"India"}
>>> x
{1: 'java', 2: 'python', 3: 'India'}
>>> x[2]
'python'
>>> print(x[1])
java
>>> x.keys()
dict_keys([1, 2, 3])
>>> x.values()
dict_values(['java', 'python', 'India'])
>>> x.items()
dict_items([(1, 'java'), (2, 'python'), (3, 'India')])
>>> x.get()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x.get()
TypeError: get expected at least 1 arguments, got 0
>>> x.get(1)
'java'
>>> x.get(java)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x.get(java)
NameError: name 'java' is not defined
>>> x.get("java")
>>> x
{1: 'java', 2: 'python', 3: 'India'}
>>> for key,val in x.items():
	print(key,val)

	
1 java
2 python
3 India
>>> dct=dict()
>>> for i in range(5):
	k=input("Enter key ")
	v=input("Enter value ")
	dct[k]=v

	
Enter key 1
Enter value 34
Enter key 2
Enter value 57
Enter key 1
Enter value 89
Enter key 3
Enter value 42
Enter key 4
Enter value 90
>>> dct
{'1': '89', '2': '57', '3': '42', '4': '90'}
>>> for i in range(5):
	k=input("Enter key ")
	v=int(input("Enter value "))
	dct[k]=v

	
Enter key 1
Enter value 1
Enter key 2
Enter value 2
Enter key 3
Enter value 3
Enter key 4
Enter value 4
Enter key 5
Enter value 5
>>> dct
{'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
>>> d2={'a':10,'b':200}
>>> d2['i']=range(1,6)
>>> d2['t']=tuple(sorted(range(9,16),reverse=True))
>>> d2
{'a': 10, 'b': 200, 'i': range(1, 6), 't': (15, 14, 13, 12, 11, 10, 9)}
>>> for k,v in d2:
	print(k,":",v)

	
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    for k,v in d2:
ValueError: not enough values to unpack (expected 2, got 1)
>>> for k,v in d2.items:
	print(k,":",v)

	
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    for k,v in d2.items:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for k,v in d2.items:
	print(k,":",v)

	
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    for k,v in d2.items:
TypeError: 'builtin_function_or_method' object is not iterable
>>> d2['t']=tuple(sorted(range(9,16),reverse=True))
>>> d2
{'a': 10, 'b': 200, 'i': range(1, 6), 't': (15, 14, 13, 12, 11, 10, 9)}
>>> {'a': 10, 'b': 200, 'i': range(1, 6), 't': (15, 14, 13, 12, 11, 10, 9)}
{'a': 10, 'b': 200, 'i': range(1, 6), 't': (15, 14, 13, 12, 11, 10, 9)}
>>> 
>>> for k,v in d2.items():
	print(k,":",v)

	
a : 10
b : 200
i : range(1, 6)
t : (15, 14, 13, 12, 11, 10, 9)
>>> lst=[]
>>> lst.append(d2)
>>> lst.append(d2)
>>> lst
[{'a': 10, 'b': 200, 'i': range(1, 6), 't': (15, 14, 13, 12, 11, 10, 9)}, {'a': 10, 'b': 200, 'i': range(1, 6), 't': (15, 14, 13, 12, 11, 10, 9)}]
>>> 
>>> for elem in lst:
	for k,v in elem.items():
		print(k,":",v)

		
a : 10
b : 200
i : range(1, 6)
t : (15, 14, 13, 12, 11, 10, 9)
a : 10
b : 200
i : range(1, 6)
t : (15, 14, 13, 12, 11, 10, 9)
>>> for elem in lst:
	for k,v in elem.items():
		print("-------")
		print(k,":",v)

		
-------
a : 10
-------
b : 200
-------
i : range(1, 6)
-------
t : (15, 14, 13, 12, 11, 10, 9)
-------
a : 10
-------
b : 200
-------
i : range(1, 6)
-------
t : (15, 14, 13, 12, 11, 10, 9)
>>> for elem in lst:
	print("-------")
	for k,v in elem.items():
		print(k,":",v)

		
-------
a : 10
b : 200
i : range(1, 6)
t : (15, 14, 13, 12, 11, 10, 9)
-------
a : 10
b : 200
i : range(1, 6)
t : (15, 14, 13, 12, 11, 10, 9)
>>> 
-------
SyntaxError: invalid syntax
>>> 
>>> dict={'Tim':10,'Charlie':22,'tiffany':23}
>>> dict.update({'Sarah':19})
>>> dict
{'Tim': 10, 'Charlie': 22, 'tiffany': 23, 'Sarah': 19}
>>> dict.update({'Sarah':20})
>>> dict
{'Tim': 10, 'Charlie': 22, 'tiffany': 23, 'Sarah': 20}
>>> del dict['Charlie']
>>> dict
{'Tim': 10, 'tiffany': 23, 'Sarah': 20}
>>> dict
{'Tim': 10, 'tiffany': 23, 'Sarah': 20}
>>> 
=========== RESTART: C:/Python37/Prog/Sorting by value in dict.py ===========
Traceback (most recent call last):
  File "C:/Python37/Prog/Sorting by value in dict.py", line 8, in <module>
    values=Dict,value()
NameError: name 'value' is not defined
>>> 
=========== RESTART: C:/Python37/Prog/Sorting by value in dict.py ===========
Traceback (most recent call last):
  File "C:/Python37/Prog/Sorting by value in dict.py", line 8, in <module>
    values=Dict,values()
NameError: name 'values' is not defined
>>> 
=========== RESTART: C:/Python37/Prog/Sorting by value in dict.py ===========
Tim : 10
Sarah : 20
Charlie : 22
tiffany : 23
>>> Dict{'Tim': 10, 'Charlie': 22, 'tiffany': 23, 'Sarah': 20
     
SyntaxError: invalid syntax
>>> Dict
{'Tim': 10, 'Charlie': 22, 'tiffany': 23, 'Sarah': 20}
>>> s=[(k.Dict[k]) for k in sorted (Dict,key=Dict.get)]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    s=[(k.Dict[k]) for k in sorted (Dict,key=Dict.get)]
  File "<pyshell#110>", line 1, in <listcomp>
    s=[(k.Dict[k]) for k in sorted (Dict,key=Dict.get)]
AttributeError: 'str' object has no attribute 'Dict'
>>> s=[(k.Dict[k]) for k in sorted (Dict,key=Dict.get)]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    s=[(k.Dict[k]) for k in sorted (Dict,key=Dict.get)]
  File "<pyshell#111>", line 1, in <listcomp>
    s=[(k.Dict[k]) for k in sorted (Dict,key=Dict.get)]
AttributeError: 'str' object has no attribute 'Dict'
>>> 
>>> 
>>> 
>>> 
