Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
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
#count()
a="twinkle twinkle little star"
a.count("twnikle")
0
a.count("twinkle")
2
a.count(t)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count(t)
NameError: name 't' is not defined
a.count('t')
5
a.count("i")
3
a.count("star")
1
b="Python python"
b.count("python")
1
b.count("Python")
1
b.count('t')
2
b.count("P")
1
#find a string
a="code"
a[0]
'c'
a.find("a")
-1
a.find("d")
2
a.find('e')
3
b="hello"
b.find("h")
0
b.find("l")
2
b[2:4]
'll'
b.find('l')
2
#escape sequences
a="name\nmobile number\tmail id\nclg"
print(a)
name
mobile number	mail id
clg
b="name:Divya\nmobile number:8939201347\tmail id:divya@12345\nclg:pvpsit"
print(b)
name:Divya
mobile number:8939201347	mail id:divya@12345
clg:pvpsit
c="name-sajad\mobile number:9278491037\tmail id:sajad@56789\nclg:pvpsit"
print(c)
name-sajad\mobile number:9278491037	mail id:sajad@56789
clg:pvpsit
c="name-sajad\nmobile number:9278491037\tmail id:sajad@56789\nclg:pvpsit"
print(c)
name-sajad
mobile number:9278491037	mail id:sajad@56789
clg:pvpsit
c="name-sajad\nmobile number-9278491037\tmail id-sajad@56789\nclg-pvpsit"
print(c)
name-sajad
mobile number-9278491037	mail id-sajad@56789
clg-pvpsit
#replace()
a="wait until your suceed"
a.replace("wait","work")
'work until your suceed'
a
'wait until your suceed'
a.replace("wait","work")
'work until your suceed'
b="wait wait until your suceed"
b.replace("wait","work")
'work work until your suceed'
b.replace("wait","work",1)
'work wait until your suceed'
c="python futhon"
c.replace("o","l")
'pythln futhln'
#lower()
a="hello"
a.upper()
'HELLO'
a[0].upper()
'H'
a.captialize()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
a.capitalize()
'Hello'
#upper()
#lower()
b="On"
b.upper()
'ON'
c="Namaste"
c.lower()
'namaste'
c="DATE"
c.lower()
'date'
c[1].lower()
'a'
d="PUNE"
d.upper()
'PUNE'
e="kashmir"
e.lower()
'kashmir'
e.captialize()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    e.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
e.capitalize()
'Kashmir'
a="python course"
a.title()
'Python Course'
b="i am in a class"
b.title()
'I Am In A Class'
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
a.isalnum()
True
b="python course"
b="PYthon course"
b.isupper()
False
b="PYTHON COURSE"
b.isupper()
True
b.islower()
False
b.isdigit()
False
b.isalpha()
False
b.isalnum()
False
c=1234
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="12345"
c.isdigit()
True
c.isalnum()
True
d="pythoncourse1234"
d.isalpha()
False
d.isalnum()
True
e="javacourse"
e.isalpha()
True
g="pooja@#123"
g.isalnum()
False
a="hello python"
a.startswith("h")
True
a.startswith("n")
False
a.endswith("n")
True
a.endswith("o")
False
>>> #strip()
>>> #lstrip(),rstrip()
>>> a="         Hello                 "
>>> a.strip()
'Hello'
>>> a.lstrip()
'Hello                 '
>>> a.rstrip()
'         Hello'
>>> b="                                                     good morning                                              "
>>> b.strip()
'good morning'
>>> b.lstrip()
'good morning                                              '
>>> b.rstrip()
'                                                     good morning'
>>> #split()
>>> a="codegnan"
>>> a.split()
['codegnan']
>>> b="Java python c c++
SyntaxError: unterminated string literal (detected at line 1)
>>> b="Java python c c++"
>>> b.split()
['Java', 'python', 'c', 'c++']
>>> c="i am in java"
>>> c.split()
['i', 'am', 'in', 'java']
>>> 
>>> #join()
>>> a="vja Hyd Vzg"
>>> a.join()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
>>> "".join(a)
'vja Hyd Vzg'
>>> b="vja","hyd","vzg"
>>> "".join(b)
'vjahydvzg'
>>> "k".join(a)
'vkjkak kHkykdk kVkzkg'
>>> "k".join(b)
'vjakhydkvzg'
