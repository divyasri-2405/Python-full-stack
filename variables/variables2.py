Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
'''variables'''
'variables'
"""variables"""
'variables'
'''5555'''
'5555'
m=10
print(m)
10
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=2,3
print(a+b)
5
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(c)
10
p=11
print(p)
11
print(a,b,c)
10 10 10
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=2,3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 7)
a,b,c=(3,4,5)
>>> print(a,b,c)
3 4 5
>>> first name="pooja"
SyntaxError: invalid syntax
>>> first_name="pooja"
>>> print(first_name)
pooja
>>> firstname="pooja"
>>> print(firstname)
pooja
>>> fname="divya"
>>> lname="ms"
>>> print(fname+lname)
divyams
>>> print(fname+" "+lname)
divya ms
>>> print(fname,lname)
divya ms
>>> fina='jdsh'
>>> lna="hdjd"
>>> kkkna='dmak'
>>> print(fina+lna+kkkna)
jdshhdjddmak
>>> name="divya"
>>> print(name)
divya
>>> NAME="pooja"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> print(NAME)
pooja
>>> Name="mds"
>>> print(Name)
mds
>>> a=8
>>> print(a)
8
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
