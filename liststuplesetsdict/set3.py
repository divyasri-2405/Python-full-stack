Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={3,4.9,"hi",8+5j,True}
print(a)
{True, 3, 4.9, 'hi', (8+5j)}
type(a)
<class 'set'>
a={1,2,3,4,5}
b=(3,4,5,6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
a={1,2,3,4,5,6}
b={3,4,5,6}
a.issubset(b)
False
b.issubset(a)
True
a.issuperset(b)
True
b.issuperset(a)
False
a={1,2,4,5,8,2,3,9}
b={9,4,7,11,19,10}
a.intersection(b)
{9, 4}
b.intersection(a)
{9, 4}
a={1,3,4,56,77,2}
b={0,3,5,1,2}
b.intersection(a)
{1, 2, 3}
a.difference(b)
{56, 4, 77}
b.difference(a)
{0, 5}
a.symmetric_difference(b)
{0, 4, 5, 56, 77}
a={2,5,3,9,0,8}
b={6,7,8,9,18}
b.symmetric_difference(a)
{0, 2, 3, 5, 6, 7, 18}
a={1,2,3}
b={4,5,6,2}
a.update(b)
a
{1, 2, 3, 4, 5, 6}
b
{2, 4, 5, 6}
a={4,5,6,3,7}
b={1,2,3}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7}
a={1,2,3,7,8,19,0}
b={2,3,7,9,10,11,5}
a.intersection_update(b)
a
{2, 3, 7}
b
{2, 3, 5, 7, 9, 10, 11}
a={2,4,6,19,1}
b={2,3,6}
b.intersection_update(a)
b
{2, 6}
a={5,7,9,10,11}
b={2,4,8,10,5}
a.difference_update(b)
a
{7, 9, 11}
b
{2, 4, 5, 8, 10}
a={7,10,82,77,1}
b={1,10,18,19,25}
>>> b.difference_update(a)
>>> b
{18, 19, 25}
>>> a={23,1,8,19,2}
>>> b={2,3,8,14,11}
>>> a.symmetric_difference_update(b)
>>> a
{1, 19, 3, 23, 11, 14}
>>> b
{2, 3, 8, 11, 14}
>>> a={2,3,1,8,9}
>>> b={2,9,0,7,6}
>>> b.symmetric_difference_update(a)
>>> b
{0, 1, 3, 6, 7, 8}
>>> a={1,2,3,7,10,5}
>>> a.discard(7)
>>> a
{1, 2, 3, 5, 10}
>>> a.copy()
{1, 2, 3, 5, 10}
>>> b=a.copy()
>>> b
{1, 2, 3, 5, 10}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> type(b)
<class 'set'>
>>> a={1,2,3,4,9}
>>> b={0,5,6,7,8}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(a)
True
