Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> hello
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> x = "hello"
>>> x
'hello'
>>> clr
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> name="Aditya"
>>> age =22
>>> "my name is a %s and my age is %d"%(name,age)
'my name is a Aditya and my age is 22'
>>> "my name is a {} and my age is {}".format(name, age)
'my name is a Aditya and my age is 22'
>>> "{} {} {}".format(*"abc")
'a b c'
>>>  "xaxis={}yaxis={}".format(**("xaxis":123,"yaxis":400))
 
SyntaxError: unexpected indent
>>> "xaxis={xaxis} yaxis={yaxis}".format(**("xaxis":123,"yaxis":400))
SyntaxError: invalid syntax
>>> "xaxis={xaxis} yaxis={yaxis}".format(**{"xaxis":123,"yaxis":400})
'xaxis=123 yaxis=400'
>>> "xaxis={xaxis} yaxis={yaxis}".format(**{"xaxis":123,"yaxis":40})
'xaxis=123 yaxis=40'
>>> "xaxis={xaxis} yaxis={yaxis}".format(**{"xaxis":123,"yaxi":400})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    "xaxis={xaxis} yaxis={yaxis}".format(**{"xaxis":123,"yaxi":400})
KeyError: 'yaxis'
>>> "xaxis={xaxis} yaxis={yaxis}".format(**{"xaxis":123,"yaxis":400})
'xaxis=123 yaxis=400'
>>> "xaxis={xaxis} yaxis={yaxis}".format(**{"yaxis":400,"xaxis":123})
'xaxis=123 yaxis=400'
>>> arr=[10,20,30]
>>> arr[]
SyntaxError: invalid syntax
>>> "{0:d}{0:b}{0:o}{0:x}".format(15)
'15111117f'
>>> "{0:d} {0:b} {0:o} {0:x}".format(15)
'15 1111 17 f'
>>> "${:,}".format(123456789)
'$123,456,789'
>>> 
