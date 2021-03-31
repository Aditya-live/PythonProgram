Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> fptr=open("C:\\Python37\\fileh\\test.txt","w")
>>> type(fptr)
<class '_io.TextIOWrapper'>
>>> fptr
<_io.TextIOWrapper name='C:\\Python37\\fileh\\test.txt' mode='w' encoding='cp1252'>
>>> fptr.close
<built-in method close of _io.TextIOWrapper object at 0x000001D6B89332D0>
>>> fptr.close()
>>> fptr.closed()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fptr.closed()
TypeError: 'bool' object is not callable
>>> fptr.closed
True
>>> fptr=open("c:/Python37/fileh/test.txt","r")
>>> fptr.close()
>>> 
>>> fptr=open("c:/Python37/fileh/test.txt","w")
>>> fptr.write("File handling demo")
18
>>> fptr.close()
>>> fptr=open("c:/Python37/fileh/test.txt","w")
>>> fptr.write("Hello world")
11
>>> fptr.close()
>>> fptr=open("c:/Python37/fileh/test.txt","a")
>>> fptr.write(" of python")
10
>>> fptr.close()
>>> 
>>> 
>>> fp=open("C:\Python37\fileh\text.txt","r")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    fp=open("C:\Python37\fileh\text.txt","r")
OSError: [Errno 22] Invalid argument: 'C:\\Python37\x0cileh\text.txt'
>>> fp=open("C:/Python37/fileh/text.txt","r")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fp=open("C:/Python37/fileh/text.txt","r")
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Python37/fileh/text.txt'
>>> fp=open("C:/Python37/fileh/text.txt")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fp=open("C:/Python37/fileh/text.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Python37/fileh/text.txt'
>>> fp=open("C://Python37//fileh//test.txt")
>>> fp.read()
'Hello world of python. Self care is must. You can be anyone you want to be but choose to be you.'
>>> print(fp.read())

>>> fp.seek(0)
0
>>> print(fp.read())
Hello world of python. Self care is must. You can be anyone you want to be but choose to be you.
>>> print(fp.read(10))

>>> fp.seek(0)
0
>>> print(fp.read(10))
Hello worl
>>>  # reads from beginning till the limit set in fp.read()
 
>>> print(fp.readline())
d of python. Self care is must. You can be anyone you want to be but choose to be you.u.
>>> #readline is used to read line by line. Helps in memory management.
>>> 
>>> fp.seek(0)
0
>>> fp.readlines()
['Hello world of python. Self care is must.\\n You can be anyone you want to be but choose to be you.']
>>> 
>>> lst=fp.readlines()
>>> lst[0]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    lst[0]
IndexError: list index out of range
>>> lst[1]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    lst[1]
IndexError: list index out of range
>>> lst[0]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    lst[0]
IndexError: list index out of range
>>> fp.readlines()
[]
>>> fp.seek(0)
0
>>> print(fp.read())
Hello world of python. Self care is must.
You can be anyone you want to be but choose to be you.
>>> fp.seek(0)
0
>>> lst=fp.readlines()
>>> lst[0]
'Hello world of python. Self care is must.\n'
>>> for i in lst:
	print(i)

	
Hello world of python. Self care is must.

You can be anyone you want to be but choose to be you.
>>> 
>>> 
>>> fp=open("c:/Python37/fileh/test.text","w")
>>> fp.write(lst)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    fp.write(lst)
TypeError: write() argument must be str, not list
>>> fp.writelines(lst)
>>> fp.close()
>>> fp=open("c:/Python37/fileh/test.text","r")
>>> fp.read()
'Hello world of python. Self care is must.\nYou can be anyone you want to be but choose to be you.'
>>> # writelines is used to write elements of list to the file.
>>> lst=["James","Blake","King","Raja"]
>>> fp.writelines(lst)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    fp.writelines(lst)
io.UnsupportedOperation: not writable
>>> lst
['James', 'Blake', 'King', 'Raja']
>>> fp.close()
>>> fp=open("c:/Python37/fileh/test.text","w")
>>> fp.writeline(lst)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    fp.writeline(lst)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'
>>> fp.writelines(lst)
>>> fp.close()
>>> fp=open("c:/Python37/fileh/test.txt","w")
>>> fp.writelines(lst)
>>> fp.close()
>>> 
>>> fp=open("c:/Python37/fileh/test.txt","r+")
>>> print(fp.read())
James
Blake
King
Raja
>>> fp.write("\nNeena")
6
>>> fp.write("\nChintoo")
8
>>> fp.seek(0)
0
>>> print(fp.read())
James
Blake
King
Raja
Neena
Chintoo
>>> fp.close()
>>> fp=open("c:/Python37/fileh/test.txt","r+")
>>> fp.write("\nAalok")
6
>>> fp.read()
'Blake\nKing\nRaja\nNeena\nChintoo'
>>> fp.seek(0)
0
>>> print(fp.read())

AalokBlake
King
Raja
Neena
Chintoo
>>> fp=open("c:/Python37/fileh/test.txt","w+")
>>> fp.write("Hello world")
11
>>> fp.seek(0)
0
>>> print(fp.read())
Hello world
>>> fp.seek(0)
0
>>> fp.write("Bye  ")
5
>>> fp.seek(0)
0
>>> print(fp.read())
Bye   world
>>> 
=============== RESTART: C:/Python37/Prog/testfile handling.py ===============
Traceback (most recent call last):
  File "C:/Python37/Prog/testfile handling.py", line 5, in <module>
    fp.write(10)
TypeError: write() argument must be str, not int
>>> 
=============== RESTART: C:/Python37/Prog/testfile handling.py ===============
>>> 
=============== RESTART: C:/Python37/Prog/testfile handling.py ===============
Traceback (most recent call last):
  File "C:/Python37/Prog/testfile handling.py", line 6, in <module>
    fp.write(i)
TypeError: write() argument must be str, not int
>>> 
