Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=19
name=a+b
>>> prin(a+b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    prin(a+b)
NameError: name 'prin' is not defined. Did you mean: 'print'?
>>> print(a+b)
29
>>> del(name)
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> if name=19
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> _fan=19
>>> print(Afan)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(Afan)
NameError: name 'Afan' is not defined. Did you mean: '_fan'?
>>> print(_fan)
19
>>> input("what is your name? ")
what is your name? sajad
'sajad'
>>> a="name"
>>> print(a)
name
>>> name="divya"
>>> name1="sajad"
>>> print(name+name1)
divyasajad
>>> jan=input("what is your name? ")
what is your name? mds
>>> print("Hi"+" "+name)
Hi divya
>>> print("Hi"+" "+jan)
Hi mds
