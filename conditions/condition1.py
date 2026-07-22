#conditions
#if-condition by using comparison operators
#<,>,<=,>=,!=,==
a=10
b=20
if a<b:
    print("true")

a=20
b=20
if a>b:
    print("true")

a=5
b=7
if a<=b:
    print("less")

a=12
b=15
if a>=b:
    print("true")

a=30
b=40
if a!=b:
    print("true")

a=10
b=10
if a==b:
    print("true")

a="python"
if a=="python":
    print("match")

a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")

a=int(input("a value"))
if a<50:
    print("less")


#if-condition by using logical operators
#and,or,not
a=6
b=3
if a<b and b>a:
    print("true")

a=4
b=7
if a<=b and b>=a:
    print("true")

a=9
b=12
if a!=b and a==b:
    print("true")

a=2
b=4
if a<b or b>a:
    print("true")

a=14
b=16
if a<=b or b>=a:
    print("true")

a=3
b=6
if a!=b or a==b:
    print("true")

a=5
b=7
if not a<b:
    print("true")

a=3
b=6
if not a>b:
    print("true")

a=3
b=6
if not a<b and b>a:
    print("true")

a=6
b=6
if not a<b or b>a:
    print("true")


#if-condition by using identify operators
#is,is not
a=4
if type(a) is int:
    print("is is int")

a=4
if type(a) is not int:
    print("is is int")

a=4.9
if type(a) is float:
    print("is float")

a=5.6
if type(a) is not float:
    print("is float")

a="stream"
if type(a) is str:
    print("is str")

a="Queen"
if type(a) is not str:
    print("is str")

a=5+9j
if type(a) is complex:
    print("is complex")

a=9+7j
if type(a) is not complex:
    print("is complex")

a=True
if type(a) is bool:
    print("is bool")

a=False
if type(a) is not bool:
    print("is bool")

a=int(input())
if type(a) is int:
    print("is int")

a=int(input())
if type(a) is not int:
    print("is int")

#if-condition by using membership operators
a=2,3,4,5,6,7,8
if 8 in a:
    print("true")

a=2,3,4,5,6,7,8
if 20 not in a:
    print("true")

a=2,3,4,5,6,7,8
b=int(input("value"))
if b in a:
    print("true")

a=int(input("a value"))
if 30 in a:
    print("true") #error


#if-else conditions using comparision operators
a=4
b=5
if a<b:
    print("less")
else:
    print("false")

a=4
b=5
if a>b:
    print("less")
else:
    print("false")

a=3
b=7
if a<=b:
    print("True")
else:
    print("False")

a=9;b=15
if a>=b:
    print("True")
else:
    print("False")

a=6;b=9
if a==b:
    print("True")
else:
    print("False")

a=8;b=1
if a!=b:
    print("True")
else:
    print("False")

a=int(input())
b=int(input())
if a<b:
    print("True")
else:
    print("False")

a=int(input())
if a<70:
    print("True")
else:
    print("False")
    
