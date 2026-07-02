Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="vijayawada"
a[0]
'v'
a[8]
'd'
a[10]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[10]
IndexError: string index out of range
a[5]
'a'
a[9]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a[0]+1
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[0]+1
TypeError: can only concatenate str (not "int") to str
b="I am in a class"
b[0]
'I'
b[1]
' '
b[1]+b[4]+b[7]
'   '
b[2]+b[3]
'am'
c=I am learning Python Course
SyntaxError: invalid syntax
c="I am learning Python Course"
c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'Python'
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> c[21]+c[22]+c[23]+c[24]+c[25]+c[26]
'Course'
>>> d="Time is very Precious"
>>> d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]
'Precious'
>>> d[8]+d[9]+d[10]+d[11]+d[12]
'very '
>>> d[8]+d[9]+d[10]+d[11]
'very'
>>> d[0]+d[1]+d[2]+d[3]
'Time'
>>> a[-1]
'a'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'wada'
>>> a="Simple is better than complex"
>>> a[-29]+a[-28]+a[-27]+[-26]+a[-25]+a[-24]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[-29]+a[-28]+a[-27]+[-26]+a[-25]+a[-24]
TypeError: can only concatenate str (not "list") to str
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'Simple'
>>> a[-12]+a[-11]+a[-10]+a[-9]
'than'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
>>> a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
>>> b="I love python
SyntaxError: unterminated string literal (detected at line 1)
>>> b="I love python"
>>> b[-13]
'I'
>>> b[-1]+b[-2]+b[-3]+b[-4]+b[-5]+b[-6]
'nohtyp'
>>> b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'python'
>>> b[-11]+b[-10]+b[-9]+b[-8]+b[-7]
'love '
>>> b[-11]+b[-10]+b[-9]+b[-8]
'love'
