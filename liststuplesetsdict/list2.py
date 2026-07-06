Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[1,4,5,6,88,99]
a.pop()
99
a
[1, 4, 5, 6, 88]
a.pop(3)
6
a
[1, 4, 5, 88]
a.remove()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> a.remove(5)
>>> a
[1, 4, 88]
>>> b=["HI","hello","Hai","namaste"]
>>> b.remove("Hi")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b.remove("Hi")
ValueError: list.remove(x): x not in list
>>> b.remove("HI")
>>> b
['hello', 'Hai', 'namaste']
>>> #len()
>>> a=["divya","sajad","advaty","adrash","varna"]
>>> len(a)
5
>>> a="divya"
>>> a=["divya","sajad","advaty","adrash","varna"]
>>> len(a)
5
>>> b="divya"
>>> len(b)
5
>>> c=["sajad"]
>>> len(c)
1
>>> b=[]
>>> b.append("hi")
>>> len(b)
1
>>> b
['hi']
>>> len(b)
1
>>> b.clear()
>>> b
[]
