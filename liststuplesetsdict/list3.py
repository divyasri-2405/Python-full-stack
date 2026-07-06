Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[1,2,3,5,9]
print(a)
[1, 2, 3, 5, 9]
type(a)
<class 'list'>
a=[4]
print(a)
[4]
type(a)
<class 'list'>
a=["ml","c","c++","java"]
print(a)
['ml', 'c', 'c++', 'java']
a.append("python")
a
['ml', 'c', 'c++', 'java', 'python']
a.append(["flask","ds"])
a
['ml', 'c', 'c++', 'java', 'python', ['flask', 'ds']]
a.extend(["django","se","UX"])
a
['ml', 'c', 'c++', 'java', 'python', ['flask', 'ds'], 'django', 'se', 'UX']
b=["vzg","hyd","vjd"]
b.insert(1,"pune")
b
['vzg', 'pune', 'hyd', 'vjd']
b.index("vzg")
0
b.index("pune")
1
b.copy()
['vzg', 'pune', 'hyd', 'vjd']
a=b.copy()
a
['vzg', 'pune', 'hyd', 'vjd']
a=[1,3,4,5,6,3,6]
a.count(1)
1
a.count(3)
2
a=["grapes","mango","apple","orange"]
a.sort()
a
['apple', 'grapes', 'mango', 'orange']
b=[1,8,-1,3,0,55,70,23]
b.sort()
b
[-1, 0, 1, 3, 8, 23, 55, 70]
>>> b.reverse()
>>> b
[70, 55, 23, 8, 3, 1, 0, -1]
>>> a=[1,8,3,4,9,0]
>>> a.reverse()
>>> a
[0, 9, 4, 3, 8, 1]
>>> a.pop()
1
>>> a
[0, 9, 4, 3, 8]
>>> a.pop(2)
4
>>> a
[0, 9, 3, 8]
>>> a.remove(3)
>>> a
[0, 9, 8]
>>> b=['a','b','r','j','k']
>>> b.remove("b")
>>> b
['a', 'r', 'j', 'k']
>>> a=["hi","hello","namaste"]
>>> len(a)
3
>>> a.clear()
>>> a
[]
>>> a=[1,2.3,"str",7+8j,True]
>>> a
[1, 2.3, 'str', (7+8j), True]
>>> a=(1,4.5,"hi",7+9j,True)
>>> print(a)
(1, 4.5, 'hi', (7+9j), True)
>>> a.index(True)
0
>>> a.index(1)
0
