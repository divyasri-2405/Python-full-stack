Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types conversion
#int
int(9)
9
int(8.7)
8
int("name")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("name")
ValueError: invalid literal for int() with base 10: 'name'
int(7j+6)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(7j+6)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
#float
float(4)
4.0
float(3.5)
3.5
float("Hi")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float("Hi")
ValueError: could not convert string to float: 'Hi'
float(4+3j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(4+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(False)
0.0
#string
str(4)
'4'
str(9.8)
'9.8'
str(hello)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    str(hello)
NameError: name 'hello' is not defined. Did you mean: 'help'?
str("Hello")
'Hello'
str('good')
'good'
str('''morning''')
'morning'
str("""Bad""")
'Bad'
str(9j+8)
'(8+9j)'
str('4')
'4'
str("7.5")
'7.5'
str("8+6j")
'8+6j'
str('7j+5')
'7j+5'
str(True)
'True'
>>> str("False")
'False'
>>> #complex
>>> complex(1)
(1+0j)
>>> complex(6.4)
(6.4+0j)
>>> complex("Good")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex("Good")
ValueError: complex() arg is a malformed string
>>> complex(8+7j)
(8+7j)
>>> complex(8j+6)
(6+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(5)
True
>>> bool(-8)
True
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(3.4)
True
>>> bool("Hello")
True
>>> bool(8j+9)
True
>>> bool(4+8j)
True
>>> bool(False)
False
>>> bool(1)
True
>>> bool(0)
False
>>> bool(True)
True
