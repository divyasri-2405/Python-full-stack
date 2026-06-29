Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data Types
a=10
type(a)
<class 'int'>
b=4.5
type(b)
<class 'float'>
c="divya"
type(c)
<class 'str'>
d='sajad'
type(d)
<class 'str'>
>>> e='''mdsmlsk'''
>>> type(e)
<class 'str'>
>>> f=9+8i
SyntaxError: invalid decimal literal
>>> f=9+8j
>>> type(f)
<class 'complex'>
>>> g=11j
>>> type(g)
<class 'complex'>
>>> h=15j+18
>>> type(h)
<class 'complex'>
>>> jk=true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    jk=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> jk="true"
>>> type(jk)
<class 'str'>
>>> lk="False"
>>> type(lk)
<class 'str'>
>>> dd=False
>>> type(dd)
<class 'bool'>
>>> ss=True
>>> type(ss)
<class 'bool'>
>>> #data type conversions
>>> #int
>>> int(9)
9
>>> int(8.7)
8
>>> int("name")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int("name")
ValueError: invalid literal for int() with base 10: 'name'
>>> hj=True
>>> type(hj)
<class 'bool'>
