Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=5;b=9
a&b
1
bin(a)
'0b101'
bin(b)
'0b1001'
bin(a&b)
'0b1'
a=8;b=3
bin(a)
'0b1000'
bin(b)
'0b11'
a|b
11
bin(a|b)
'0b1011'
a=16
-(a+1)
-17
~a
-17
bin(-(a+1))
'-0b10001'
bin(~a)
'-0b10001'
a=8
~a
-9
bin(~a)
'-0b1001'
s=-19
~s
18
bin(s)
'-0b10011'
>>> bin(~s)
'0b10010'
>>> g=7;f=3
>>> g^f
4
>>> bin(g)
'0b111'
>>> bin(f)
'0b11'
>>> bin(g^f)
'0b100'
>>> a=3
>>> a<<2
12
>>> bin(a)
'0b11'
>>> bin(a<<2)
'0b1100'
>>> b=4
>>> bin(b)
'0b100'
>>> b<<3
32
>>> bin(b<<3)
'0b100000'
>>> a=6
>>> bin(a)
'0b110'
>>> a>>3
0
>>> bin(a>>3)
'0b0'
>>> a=8
>>> bin(a)
'0b1000'
>>> a>>2
2
>>> bin(a)
'0b1000'
