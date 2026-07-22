#conditions
#if-condition using comparison operators
#<,>,<=,>=,==,!=
a=10;b=20
if a<b:
    print("True")
if a>b:
    print("True")
a=12;b=11
if a<=b:
    print("less")
if a>=b:
    print("less")
if a!=b:
    print("true")
if a==b:
    print("true")
a=int(input())
b=int(input())
if a<b:
    print("less")
if a>b:
    print("less")
if a<=b:
    print("true")
if a>=b:
    print("true")
if a!=b:
    print("true")
if a==b:
    print("less")
a="python"
if a=="python":
    print("true")
a=str(input())
if a=="Python":
    print("true")
a=int(input("a value: "))
b=int(input("b value: "))
if a<b:
    print("less")
if a>b:
    print("less")
if a<=b:
    print("true")
if a>=b:
    print("true")
if a==b:
    print("less")
if a!=b:
    print("true")
a=int(input())
if a<50:
    print("true")
a=50
if a<70:
    print("true")
    
#if-condition by using logical operators
#or,and,not
a=6
b=3
if a<b and b>a:
    print("true")
if a<=b and b>=a:
    print("true")
if a<b or b>a:
    print("true")
if a<=b or b>=a:
    print("less")
if a==b and a!=b:
    print("less")
if a==b or a!=b:
    print("true")
if not a<b:
    print("less")
if not a>b:
    print("true")
if not a<b and b>a:
    print("true")
if not a<=b and b>=a:
    print("less")
if not a==b and a!=b:
    print("true")
if not a<b or a>b:
    print("true")
if not a<=b or a>=b:
    print("less")
if not a==b or a!=b:
    print("less")
a=int(input())
b=int(input())
if a<b and b>a:
    print("less")
if a<=b and b>=a:
    print("less")
if a==b and a!=b:
    print("less")
if a<b or b>a:
    print("true")
if a<=b or b>=a:
    print("true")
if a==b or a!=b:
    print("true")
if not a<b:
    print("less")
if not a>b:
    print("less")
if not a<b and b>a:
    print("true")
if not a<b or b>a:
    print("true")

#if-condition by using identify operators
#is,is not
a=7
if type(a) is int:
    print("is int")
if type(a) is not int:
    print("is float")
a=39.8
if type(a) is float:
    print("is float")
if type(a) is not float:
    print("is float")
a="Hi"
if type(a) is str:
    print("is str")
if type(a) is not str:
    print("is str")
a=3+8j
if type(a) is complex:
    print("is complex")
if type(a) is not complex:
    print("is complex")
a=True
if type(a) is bool:
    print("is boolean")
if type(a) is not bool:
    print("is boolean")
a=int(input())
if type(a) is int:
    print("is int")
if type(a) is not int:
    print("is int")

#if-condition by using membership operators
a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
if 20 not in a:
    print("less")
a=2,3,4,5,6,7,8
b=int(input())
if b in a:
    print("true")

#if-else conditions using comparision operators
a=9;b=3
if a<b:
    print("true")
else:
    print("false")
if a>b:
    print("true")
else:
    print("false")
if a<=b:
    print("true")
else:
    print("false")
if a>=b:
    print("true")
else:
    print("false")
if a==b:
    print("true")
else:
    print("false")
if a!=b:
    print("true")
else:
    print("false")
a=int(input())
b=int(input())
if a<b:
    print("true")
else:
    print("false")
if a>b:
    print("true")
else:
    print("false")
if a==b:
    print("true")
else:
    print("false")
if a<=b:
    print("true")
else:
    print("false")
if a>=b:
    print("true")
else:
    print("false")
if a!=b:
    print("true")
else:
    print("false")
a="python"
if a=="python":
    print("true")
else:
    print("false")
a=str(input())
if a=="Python":
    print("true")
else:
    print("false")

#if-else condition using logical operators
a=6;b=9
if a<b and b>a:
    print("true")
else:
    print("false")
if a<=b or b>=a:
    print("true")
else:
    print("false")
if a==b and a!=b:
    print("true")
else:
    print("false")
if a<=b and b>=a:
    print("true")
else:
    print("false")
if a<b or b>a:
    print("true")
else:
    print("false")
if a==b or a!=b:
    print("true")
else:
    print("false")
if not a<b and b>a:
    print("true")
else:
    print("false")
if not a<b or b>a:
    print("true")
else:
    print("false")

#if-else condition using identify operators
c=7
if type(c) is int:
    print("is int")
else:
    print("is not int")
c=4.6
if type(c) is float:
    print("is float")
else:
    print("is not float")
c="hi"
if type(c) is str:
    print("is str")
else:
    print("is not str")
c=9+8j
if type(c) is complex:
    print("is complex")
else:
    print("is not complex")
c=True
if type(c) is bool:
    print("is boolean")
else:
    print("is not boolean")
a=int(input())
if type(a) is int:
    print("is int")
else:
    print("is not int")
if type(a) is not int:
    print("is not int")
else:
    print("is int")
#if-else condition using membership operators
a=1,2,3,4,5,6,7,8,9,10
if 8 in a:
    print("true")
else:
    print("false")
if 8 not in a:
    print("true")
else:
    print("false")
a=1,2,3,4,5,6,7,8,9,10
b=int(input())
if b in a:
    print("true")
else:
    print("false")
