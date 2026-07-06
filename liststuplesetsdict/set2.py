Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={3,4,5,6,7,8}
>>> a.discard(6)
>>> a
{3, 4, 5, 7, 8}
>>> a.copy()
{3, 4, 5, 7, 8}
>>> a
{3, 4, 5, 7, 8}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> a={2,3,4,5,6}
>>> len(a)
5
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
>>> a={2,3,4,5,6,7,8}
>>> b={1,10,99,11,9}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(a)
True
