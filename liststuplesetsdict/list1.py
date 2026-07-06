Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
#list[]
a=[2,5.6,"python",8+5j,True]
print(a)
[2, 5.6, 'python', (8+5j), True]
type(a)
<class 'list'>
a=[2,4.5,"Hi",7+9j,True]
print(b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
print(a)
[2, 4.5, 'Hi', (7+9j), True]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=[4]
type(c)
<class 'list'>
a=["python","Java","c","c++"]
print(a)
['python', 'Java', 'c', 'c++']
a.append["ml"]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append["ml"]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append("ml")
a
['python', 'Java', 'c', 'c++', 'ml']
a.append("dsa","Flask")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.append("dsa","Flask")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["dsa","flask"])
a
['python', 'Java', 'c', 'c++', 'ml', ['dsa', 'flask']]
#append
#extend()
#append()
#extend()
a=["ml","ds","dsa"]
a.extend("java","python")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.extend("java","python")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["java","python"])
a
['ml', 'ds', 'dsa', 'java', 'python']
a.extend(["flask","django","se"])
a
['ml', 'ds', 'dsa', 'java', 'python', 'flask', 'django', 'se']
#insert
#inser()
#insert()
b=["vjd","Hyd"]
print(b)
['vjd', 'Hyd']
b.insert(1,"Vgz")
b
['vjd', 'Vgz', 'Hyd']
b.insert(2,Pune)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b.insert(2,Pune)
NameError: name 'Pune' is not defined
b.insert(2,"pune")
b
['vjd', 'Vgz', 'pune', 'Hyd']
#index()
b=["yellow","pink","yellow","black"]
b.index("pink")
1
b.copy()
['yellow', 'pink', 'yellow', 'black']
a=b.copy()
a
['yellow', 'pink', 'yellow', 'black']
c=a.copy()
c
['yellow', 'pink', 'yellow', 'black']
b.count("yellow")
2
#sort()
a=["grapes","pineapple","apple","orange"]
a.sort()
a
['apple', 'grapes', 'orange', 'pineapple']
b=[7,8,3,4,5,2,0,9,1]
b
[7, 8, 3, 4, 5, 2, 0, 9, 1]
b.sort()
b
[0, 1, 2, 3, 4, 5, 7, 8, 9]
c=[44,9.8,6,3,6,-1,5,0,29,34]
c.sort()
c
[-1, 0, 3, 5, 6, 6, 9.8, 29, 34, 44]
#reverse()
a=[7,8,9,33,67,89,100]
a.reverse()
a
[100, 89, 67, 33, 9, 8, 7]
b=["java","python","css"]
b
['java', 'python', 'css']
b.reverse()
b
['css', 'python', 'java']
>>> c=[9,6,37,99,100,25]
>>> c.reverse()
>>> c
[25, 100, 99, 37, 6, 9]
>>> a=["c","c++","java","python"]
>>> a.pop()
'python'
>>> a
['c', 'c++', 'java']
>>> a.pop(1)
'c++'
>>> a
['c', 'java']
>>> #pop()
>>> #remove()
>>> a.remove("c")
>>> a
['java']
>>> b=[1,5,6,99,13,19]
>>> b.pop()
19
>>> b
[1, 5, 6, 99, 13]
>>> b.pop(5)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    b.pop(5)
IndexError: pop index out of range
>>> b.pop(4)
13
>>> b.remove(3)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    b.remove(3)
ValueError: list.remove(x): x not in list
>>> b
[1, 5, 6, 99]
>>> b.remove("5")
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    b.remove("5")
ValueError: list.remove(x): x not in list
>>> b.remove(1)
>>> b
[5, 6, 99]
