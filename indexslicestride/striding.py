Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
a[::2]
'Dt cec'
a[::3]
'Dacn'
a[3:]
'a Science'
a[:9]
'Data Scie'
b="cloud computing"
b[::5]
'c u'
b[::4]
'cdmi'
b[::8]
'cm'
b[2:]
'oud computing'
b[:9]
'cloud com'
b[3:11]
'ud compu'
b[::2]
'codcmuig'
b[::6]
'cci'
c="Machine Learning"
c[1:9:2]
'ahn '



1


1
1114\41\\\1\24\
                
SyntaxError: unexpected character after line continuation character
>>> c="Machine Learning"
>>> c[3:14:2]
'hn eri'
>>> c[5:15:4]
'nei'
>>> c[2:12:3]
'cnLr'
>>> c[0:10:1]
'Machine Le'
>>> d='Python Course"
SyntaxError: unterminated string literal (detected at line 1)
>>> d="Python Course"
>>> d[-1:-10:-2]
'ero o'
>>> d[-3:-13:-4]
'r t'
>>> d[-5:-11:-3]
'on'
>>> f="python Course"
>>> a[8:6:2]
''
>>> a[6:8:2]
'c'
>>> f="python course"
>>> a[8:6:2]
''
>>> f[8:6:2]
''
>>> f[6:8:2]
' '
>>> f[6:11:2]
' or'
>>> f[-7:-4:-2]
''
>>> f[-4:-7:-2]
'uc'
>>> f[::1]
'python course'
>>> f[::1]
'python course'
>>> f[1::]
'ython course'
>>> f[::-1]
'esruoc nohtyp'
>>> f[-1::]
'e'
