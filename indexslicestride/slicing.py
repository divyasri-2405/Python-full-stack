Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a[0:8]
'codegnan'
a[:8]
'codegnan'
a[8:]
''
b="Work until you succeed"
b[5:10]
'until'
b[5:9]
'unti'
b[5:10]
'until'
b[11:14]
'you'
b[0:4]
'Work'
>>> b[15:22]
'succeed'
>>> c="codegnan it solutions"
>>> c[9:11]
'it'
>>> c[12:21]
'solutions'
>>> c[0:8]
'codegnan'
>>> d="vijayawada is a royal city"
>>> d[-10:-5]
'royal'
>>> D[-26:-16]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    D[-26:-16]
NameError: name 'D' is not defined. Did you mean: 'd'?
>>> d[-26:-16]
'vijayawada'
>>> d[-4:0]
''
>>> d[-4:-1]
'cit'
>>> d[-4:0]
''
>>> d[-4]
'c'
>>> d[-4:]
'city'
>>> e="vizag is city of destiny"
>>> e[-6:]
'estiny'
>>> e[-7:]
'destiny'
>>> e[-22:-17]
'zag i'
>>> e[-22:-17]
'zag i'
>>> e[-15:-11]
'city'
>>> e[-24:-19]
'vizag'
>>> e[-24:-19]
'vizag'
>>> e[-18:-16]
'is'
