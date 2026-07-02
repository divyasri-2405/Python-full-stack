Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="pvp siddhartha Institute of Technology"
a[::38]
'p'
a[::]
'pvp siddhartha Institute of Technology'
a[0:9]
'pvp siddh'
a[;;39]
SyntaxError: invalid syntax
a[::39]
'p'
a[::40]
'p'
a[:37]
'pvp siddhartha Institute of Technolog'
a[37:]
'y'
a[38:]
''
a[:38]
'pvp siddhartha Institute of Technology'
a[0:10]
'pvp siddha'
a[1:18]
'vp siddhartha Ins'
a[-1:-38]
''
a[-1:-37]
''
>>> a[-39:-1]
'pvp siddhartha Institute of Technolog'
>>> a[-39:]
'pvp siddhartha Institute of Technology'
>>> a[1:38]
'vp siddhartha Institute of Technology'
>>> a[0:38]
'pvp siddhartha Institute of Technology'
>>> a[-34:-1]
'siddhartha Institute of Technolog'
>>> a[-16:-5]
'te of Techn'
>>> a[:39]
'pvp siddhartha Institute of Technology'
>>> a[-38:]
'pvp siddhartha Institute of Technology'
>>> a[39:]
''
>>> a[:-38]
''
>>> a[::2]
'ppsdhrh nttt fTcnlg'
>>> f[1:16:2]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    f[1:16:2]
NameError: name 'f' is not defined
>>> a[1:16:2]
'v idataI'
>>> a[3:22:3]
' dahItu'
>>> a[-2:-16:-5]
'ghf'
>>> a[-16:-33:-1]
'tutitsnI ahtrahdd'
>>> a[-39::]
'pvp siddhartha Institute of Technology'
>>> a[::-38]
'y'
