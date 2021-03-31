Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> def show():
	print("Hello world")

	
>>> show()
Hello world
>>> def show(x,y,z):
	print("Hello world")

	
>>> show(1,2,3)
Hello world
>>> #You can pass argument to parameter function and use it later.
>>> 
>>> def show(x,y):
	z=x+y
	return z

>>> ob=show(2,4)
>>> print(ob)
6
>>> def show(x,y):
	z=x+y
	print(z)

	
>>> show(2,4)
6
>>> def show(x,y):
	i=x+y
	j=x*y
	k=x-y
	return i,j,k

>>> ob,ob1,ob2=show(2,4)
>>> print(ob,ob1,ob2)
6 8 -2
>>> #you can return miltiple values in function
>>> #No. of variables to store value= No. of values returned
>>> 
>>> 
>>> varGlobal=10
>>> def fun():
	global varGlobal
	varGlobal=0
	varLocal=0

	
>>> fun()
>>> if(varGlobal==0):
	print("Flag set to 0")

	
Flag set to 0
>>> varGlobal=10
>>> def fun():
	varGlobal=0
	varLocal=0

	
>>> fun()
>>> if(varGlobal==0):
	print("Flag set to 0")

	
>>> #If we use 'global' key word in a function then we can change the value of a global variable.
>>> def fun():
        global varGlobal
	varGlobal=0
	print(varGlobal)
	varLocal=0
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def fun():
        global varGlobal
        varGlobal=0
        print(varGlobal)
	varLocal=0
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def fun();
SyntaxError: invalid syntax
>>> def fun():
	global varGlobal
	print(varGlobal)
	varGlobal=0
	print(varGlobal)

	
>>> fun()
10
0
>>> def fun(a,b=3,c=3)
SyntaxError: invalid syntax
>>> def fun(a,b=3,c=3):
	print(a,b,c)

	
>>> fun(1)
1 3 3
>>> fun(1,5)
1 5 3
>>> fun(1,5,4)
1 5 4
>>> #the arguments passed in the function will over write the default values if present)
>>> 
>>> 
>>> def fun(a,b,c):
	print(a,b,c)

	
>>> fun(c=3,b=2,a=1)
1 2 3
>>> fun(3,2,1)
3 2 1
>>> 
>>> 
>>> def fun(*arr):
	for val in arr:
		print val
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(val)?
>>> def fun(*arr):
	for val in arr:
		print(val)

		
>>> fun(1,2,3)
1
2
3
>>> fun(1,2,3,4,5)
1
2
3
4
5
>>> #Function above with single * is used for values
>>> 
>>> 
>>> def fun(**arr):
	for k in arr.keys():
		print(k,":",arr[k])

		
>>> fun(a='xyz',b='abc')
a : xyz
b : abc
>>> #Function above with double ** is used for dictionary
>>> 1 2 3
SyntaxError: invalid syntax
>>> 
>>> 
>>> def fun(a,b,c):
	c=a+b
	print(c)

	
>>> fun(1,2,3)
3
>>> fun(1,1,3)
2
>>> def fun(a,b,c=9):
	c=a+b
	print(c)

	
>>> fun(1,1)
2
>>> def fun(a,b,c):
	c1=a+b
	print(c1)

	
>>> fun(1,2)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    fun(1,2)
TypeError: fun() missing 1 required positional argument: 'c'
>>> 
>>> #The statement in the function replaces the value of the argument
>>> 
>>> def show():
	print('Java')
	def put():
		print('Python')

		
>>> show
<function show at 0x000001B74B2916A8>
>>> show()
Java
>>> 
>>> def show():
	print('Java')
	def put():
		print('Python')
	put()

	
>>> show()
Java
Python
>>> put()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    put()
NameError: name 'put' is not defined
>>> 
>>> # The put() function didn't work because it is inside the show() function. It can be called only in show() function.
>>> 
>>> x=lambda i,j:x+j
>>> x(2,4)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    x(2,4)
  File "<pyshell#124>", line 1, in <lambda>
    x=lambda i,j:x+j
TypeError: unsupported operand type(s) for +: 'function' and 'int'
>>> x=lambda i,j:i+j
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x=lambda i,j:i+j
>>> print(x(2,4))
6
>>> x=lambda i,j=5:i+j
>>> print(x(2))
7
>>> import random
>>> random.randrange(1,10)
7
>>> random.randrange(1,10)
4
>>> random.randrange(1,10)
2
>>> random.randrange(1,10)
7
>>> random.randrange(1,10)
3
>>> #randrange exludes the last element
>>> 
>>> random.randint(1,10)
7
>>> random.randint(1,10)
9
>>> random.randint(1,10)
8
>>> #randint includes the last element as well.
>>> 
