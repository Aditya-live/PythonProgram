Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import calc
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'calc']
>>> dir(calc)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'pro', 'sub']
>>> help(calc)
Help on module calc:

NAME
    calc

DESCRIPTION
    This is a cal module
    contains basic functions
    for arithmetic operation (doc string)

FUNCTIONS
    add(num1, num2)
    
    pro(num1, num2)
    
    sub(num1, num2)

FILE
    c:\python37\calc.py


>>> help(cal.add)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    help(cal.add)
NameError: name 'cal' is not defined
>>> help(calc.add)
Help on function add in module calc:

add(num1, num2)

>>> calc.add(12,13)
25
>>> 
