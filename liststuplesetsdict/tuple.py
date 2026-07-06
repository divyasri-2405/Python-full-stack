Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(4,5.6,"Hi",8+9j,True)
>>> print(a)
(4, 5.6, 'Hi', (8+9j), True)
>>> type(a)
<class 'tuple'>
>>> b=(3,-9,6.7,"Hello",7+4j,True)
>>> b
(3, -9, 6.7, 'Hello', (7+4j), True)
>>> type(b)
<class 'tuple'>
>>> a.count(5+9j)
0
>>> a.count(8+9j)
1
>>> a.index(True)
4
>>> a.index("hello")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.index("hello")
ValueError: tuple.index(x): x not in tuple
>>> a.index("Hi")
2
>>> len(a)
5
>>> len(b)
6
