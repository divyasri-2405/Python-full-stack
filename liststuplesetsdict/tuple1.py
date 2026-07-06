Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=(1,4.5,"hi",8+2j,True)
>>> print(a)
(1, 4.5, 'hi', (8+2j), True)
>>> type(a)
<class 'tuple'>
>>> a.count(1)
2
>>> a.count(True)
2
>>> a.count(8+2j)
1
>>> a.index(True)
0
>>> a=(2,6.7,"hi",4+9j,True)
>>> print(a)
(2, 6.7, 'hi', (4+9j), True)
>>> a.index(True)
4
>>> len(a)
5
>>> len(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    len(b)
NameError: name 'b' is not defined
>>> len(a)
5
