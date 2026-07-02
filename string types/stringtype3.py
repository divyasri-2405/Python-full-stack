Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="python"
a.len()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.len()
AttributeError: 'str' object has no attribute 'len'
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
b.count(o)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b.count(o)
NameError: name 'o' is not defined
b.count('o')
2
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("i")
3
a="Python python"
a.count("python")
1
a="code"
a.find('o')
1
a.find("e")
3
a="name\nmobile no\temail id\nclg"
print(a)
name
mobile no	email id
clg
b="name:divya\nmobile no-847598345982\temail id:gfgh@gmail.com\nclg-PVpsit"
print(b)
name:divya
mobile no-847598345982	email id:gfgh@gmail.com
clg-PVpsit
a="wait wait until your succeed"
a.replace("wait","work")
'work work until your succeed'
a.replace("wait","work",1)
'work wait until your succeed'
a.lower()
'wait wait until your succeed'
a.upper()
'WAIT WAIT UNTIL YOUR SUCCEED'
a.capitalize()
'Wait wait until your succeed'
a.title()
'Wait Wait Until Your Succeed'
a="12345"
a.isdigit()
True
a="1234@#"
a.isalnum()
False
a="ghdg123"
a.isalnum()
True
a="gfdh"
a.isalpha()
True
a.islower()
True
a="GJGF"
a.isupper()
True
a="         Hello  Morning       "
a.strip()
'Hello  Morning'
a.lstrip()
'Hello  Morning       '
a.rstrip()
'         Hello  Morning'
a="Codegnan"
a.split()
['Codegnan']
a="Hi Hello Namaste Good"
a.split()
['Hi', 'Hello', 'Namaste', 'Good']
"".join(a)
'Hi Hello Namaste Good'
" ".join(a)
'H i   H e l l o   N a m a s t e   G o o d'
b="vja","ap","hyd"
"".join(b)
'vjaaphyd'
" ".join(b)
'vja ap hyd'
"k".join(b)
'vjakapkhyd'
a="Hello";b="World"
print(a+b)
HelloWorld
print(a+" "+b)
Hello World
fname="divya sri";lname="motamarri"
print(fname+lname)
divya srimotamarri
print(fname+" "+lname)
divya sri motamarri
print(fname.capitalize()+" "+lname.capitalize())
Divya sri Motamarri
print((fname+" "+lname).capitalize())
Divya sri motamarri
print(fname.title()+" "+lname.title())
Divya Sri Motamarri
print((fname+" "+lname).title())
Divya Sri Motamarri
a=5;b=6
print("the sum is",a+b)
the sum is 11
>>> a="vja"
>>> print("the city is",a)
the city is vja
>>> a="mine"
>>> print(1,a)
1 mine
>>> a="sita";b="gita"
>>> print("Hello{}{]",.format(a,b))
SyntaxError: invalid syntax
>>> print("hello{}{}".format(a,b))
hellositagita
>>> print("hello {}  {} ".format(a,b))
hello sita  gita 
>>> print("hello {}  hello  {} ".format(a,b))
hello sita  hello  gita 
>>> print(f"hello {a} {b}")
hello sita gita
>>> print(f"Hello {a}  Hello  {b}")
Hello sita  Hello  gita
>>> print(f"Hello  {a}    {b}")
Hello  sita    gita
>>> a=12;b=2
>>> mult=a*b
>>> print("The multi is {}".format(mult))
The multi is 24
>>> print("The multi is {}".format(a*b))
The multi is 24
>>> print(f"the multi is {multi}")
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(f"the multi is {multi}")
NameError: name 'multi' is not defined. Did you mean: 'mult'?
>>> print (f"the multi is {mult}")
the multi is 24
>>> print(f"the multi is {a*b}")
the multi is 24
>>> a="Hello"
>>> a.startswith()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.startswith()
TypeError: startswith expected at least 1 argument, got 0
>>> a.startswith('H')
True
>>> a.endswith('o')
True
