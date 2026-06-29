Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthimetic
a=9
b=5
print(a+b)
14
print(a-b)
4
print(a*b)
45
print(a/b)
1.8
print(a//b)
1
print(a**b)
59049
print(a%b)
4
a=4;b=9
print(a+b)
13
print(a-b)
-5
print(a*b)
36
print(a//b)
0
print(a/b)
0.4444444444444444
print(a**b)
262144
print(a%b)
4
#assignment
a=9,b=5
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=9;b=3
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
12
a-=b
b
3
a
9
a*=b
a
27
a/=b
a
9.0
a//=b
a
3.0
a**=b
a
27.0
a%=b
a
0.0
a=7;b=13
a+=b
a
20
a-=b
a
7
a*=b
a
91
a//=b
a
7
a/=b
a
0.5384615384615384
a**=b
a
0.0003198975693219886
a%=b
a
0.0003198975693219886
a=6
b=8
a+=b
a
14
a+=5
a
19
a-=7
a
12
b*=8
b
64
b/=9
b
7.111111111111111
a**=5
a
248832
a//=8
a
31104
b%=3
b
1.1111111111111107
#comparison
a=8;b=9
a<b
True
a>b
False
a==b
False
a>=b
False
a<=b
True
a!=b
True
b>a
True
b<a
False
b>=a
True
b<=a
False
a=2
b=1
a<b
False
a>b
True
b>a
False
b<a
True
a==b
False
a<=b
False
a>=b
True
b<=a
True
b>=a
False
a==b
False
a!=b
True
a=3;b=3
a==b
True
a=5;b=4
a!=b
True
#logical
a=6;b=7
a<b and b>a
True
a<=b and b>=a
True
a>b and b<a
False
a>=b and b<=a
False
a!=b and b!=a
True
a==b and b==a
False
a<b or b>a
True
a<b and b<a
False
a<=b or b<=a
True
a!=b or a<b
True
a==b or a>b
False
a>=b or a!=b
True
not true
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
a=6
type(a) is int
True
type(a) is not int
False
type(a) is str
False
type(a) is not boolean
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    type(a) is not boolean
NameError: name 'boolean' is not defined
type(a) is not bool
True
a=8.9
type(a) is float
True
type(a) is not float
False
type(a) is complex
False
type(a) is not int
True
b="bool"
type(b) is str
True
type(b) is bool
False
type(b) is not str
False
type(b) is not float
True
c=8+7j
>>> type(c) is complex
True
>>> type(c) is not complex
False
>>> type(c) is str
False
>>> type(c) is not bool
True
>>> d=True
>>> type(d) is str
False
>>> type(d) is bool
True
>>> type(d) is not bool'
SyntaxError: unterminated string literal (detected at line 1)
>>> type(d) is not bool
False
>>> type(d) is not float
True
>>> a=9,0,3,4,5,6
>>> 9 in a
True
>>> 15 in a
False
>>> 8 not in a
True
>>> 9 in a
True
>>> 6 not in a
False
>>> 0 in a
True
>>> 7 not in a
True
>>> #membership
>>> a=9,0,3,6,7,8
>>> 9 ina
SyntaxError: invalid syntax
>>> 9 in a
True
>>> 9 not in a
False
>>> 17 in a
False
>>> 17 not in a
True
