Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={1,2.3,"hi",8+9j,True}
print(a)
{1, 2.3, (8+9j), 'hi'}
b={2,3.4,"hello",8+7j,True,False}
print(b)
{False, True, 2, 3.4, 'hello', (8+7j)}
type(a)
<class 'set'>
type(b)
<class 'set'>
a={3,4,5,6,7,8}
b={4,5,6,7}
a.issubset(b)
False
b.issubset(a)
True
a.issuperset(b)
True
b.issuperser(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b.issuperser(a)
AttributeError: 'set' object has no attribute 'issuperser'. Did you mean: 'issuperset'?
b.issuperset(a)
False
#union()
a={3,4,5,6,7,8}
b={1,2,3,4,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
c={6,7,8,8,9,10,10}
print(c)
{6, 7, 8, 9, 10}
#intersection()
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
a={4,7,8,1,2}
b={7,9,4,5,1,0,2}
a.intersection(b)
{1, 2, 4, 7}
a={10,20,30,40,50,60}
b={50,60,70,80,90,100}
a.update(b)
a
{100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
b
{80, 50, 100, 70, 90, 60}
b.update(a)
b
{70, 10, 80, 20, 90, 30, 100, 40, 50, 60}
#difference()
a={1,2,3,4,5,6,7,8}
b={6,7,8,9,10,11,2}
a.difference(b)
{1, 3, 4, 5}
b.difference(a)
{9, 10, 11}
#symmetric difference()
a={3,4,5,6,7,8,9}
b={1,2,3,5,7,9,11,12}
a.symmetric_difference(b)
{1, 2, 4, 6, 8, 11, 12}
b.symmetric_difference(a)
{1, 2, 4, 6, 8, 11, 12}
a.intersection_update(b)
a
{9, 3, 5, 7}
b
{1, 2, 3, 5, 7, 9, 11, 12}
b.intersection_update(a)
b
{9, 3, 5, 7}
b
{9, 3, 5, 7}
a
{9, 3, 5, 7}
b
{9, 3, 5, 7}
a={2,3,4,5,6,7,8,9}
b={1,10,4,5,6,8,15,20}
a.difference_update(b)
a
{2, 3, 7, 9}
b.difference_update(a)
b
{1, 4, 5, 6, 8, 10, 15, 20}
a={2,3,4,5,6,7,8}
b={1,10,2,3,6,11}
b.difference_update(a)
b
{1, 10, 11}
a
{2, 3, 4, 5, 6, 7, 8}
a.difference_update(b)
a
{2, 3, 4, 5, 6, 7, 8}
a={11,13,14,6,7,9,14,15}
b={9,3,2,6,7,1,3}
a.symmetric_difference_update(b)
a
{1, 2, 3, 11, 13, 14, 15}
>>> b.symmetric_difference_update(a)
>>> b
{6, 7, 9, 11, 13, 14, 15}
>>> a={4,5,6,7,9,10,11}
>>> b={5,7,2,1,8}
>>> b.symmetric_difference_update(b)
>>> b.symmetric_difference_update(a)
>>> b
{4, 5, 6, 7, 9, 10, 11}
>>> a={4,5,6,7,8,9,10,11}
>>> b={1,2,3,4,5,6,7}
>>> b.symmetric_difference_update(a)
>>> b
{1, 2, 3, 8, 9, 10, 11}
>>> a.symmetric_difference_update(b)
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> KeyboardInterrupt
>>> a={4,5,6,7,8,9,10,11}
... b={1,2,3,4,5,6,7}
SyntaxError: multiple statements found while compiling a single statement
>>> a={4,5,6,7,8,9,10,11} b={1,2,3,4,5,6,7}
SyntaxError: invalid syntax
>>> a={2,3,4,5,6}
>>> a.pop()
2
>>> a
{3, 4, 5, 6}
>>> a.remove(4)
>>> a
{3, 5, 6}
>>> a={3,4,5,6,7,8,(}
...    
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> a={3,4,5,6,7,8,9}
...    
>>> a.copy()
...    
{3, 4, 5, 6, 7, 8, 9}
>>> a.copy()
...    
{3, 4, 5, 6, 7, 8, 9}
>>> a={3,4,5,6,7,8}
...    
>>> a={3,4,5}
...    
