#conditions
#if-elif-else
#if-elif-else using comparison operators
a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")

a=4
b=6
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")

a=10;b=20
if a>b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")

a=6
b=4
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")

a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")

#if-elif-else using logical operators
a=4
b=6
if a<b and b>a:
    print("less")
elif a>b and b<a:
    print("greater")

if a>=b and b<=a:
    print("less")
elif a<=b and b>=a:
    print("greater")
else:
    print("true")

if a>=b and b<=a:
    print("less")
elif a!=b and b>=a:
    print("greater")
else:
    print("true")

if a>=b and b<=a:
    print("less")
elif a==b and a>b:
    print("greater")
else:
    print("true")

if a<b or b>a:
    print("less")
elif a>b or b<a:
    print("greater")
else:
    print("true")

if a>=b or b<=a:
    print("greater")
elif a==b or b>=a:
    print("less")

if a!=b or a==b:
    print("greater")
elif a<=b or b>=a:
    print("greater")
else:
    print("true")

if not a<b and b>a:
    print("less")
elif not a>=b and b<=a:
    print("greater")

if not a<b:
    print("true")
elif not b>a:
    print("false")
else:
    print("less")

if not a>=b or b<=a:
    print("less")
elif not a<=b or b==a:
    print("greater")
else:
    print("true")

#if-elif-else using identify operators
a=5
if type(a) is int:
    print("is int")
elif type(b) is not int:
    print("is not int")

a=4.5
if type(a) is float:
    print("is float")
elif type(a) is not float:
    print("is not float")
else:
    print("true")

a="hi"
if type(a) is str:
    print("is str")
elif type(a) is not str:
    print("is not str")
else:
    print("true")

a=8+9j
if type(a) is complex:
    print("is complex")
elif type(a) is not complex:
    print("is not complex")

a=True
if type(a) is bool:
    print("is boolean")
elif type(a) is bool:
    print("is not boolean")
else:
    print("true")

#if-elif-else using membership operators
a=1,2,3,4,5,6,72
if 7 in a:
    print("true")
elif 7 not in a:
    print("false")

a=1,2,3,4,5,6,7,8
if 8 in a:
    print("true")
elif 8 not in a:
    print("false")
else:
    print("less")

a=1,2,3,4,5,6,7,8
b=int(input())
if b in a:
    print("true")
elif b not in a:
    print("false")
else:
    print("true")

#multiple-if conditions
#multiple-if conditions using comparison operators
a=20
b=40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")

a=20
b=40
if a==b:
    print("equal")
if b>a:
    print("greater")
if a<=b:
    print("less than equal")

a=60
b=70
if a==b:
    print("equals to")
if b>a:
    print("greater")
if a>=b:
    print("not equal")
else:
    print("true")

#multiple-if conditions using logical operators
a=40;b=90
if a<b and b>a:
    print("true")
if b>a and a<b:
    print("false")
if a==b or a!=b:
    print("else")
    
a=40;b=50
if a<=b and a>=b:
    print("less")
if a<=b and b>=a:
    print("true")
if a==b or b>=a:
    print("false")

a=80;b=90
if a<=b and b>=a:
    print("true")
if b>=a and a<=b:
    print("false")
if not a>=b or a<=b:
    print("high")
else:
    print("less")

#multiple-if conditions using membership and identify operators
a=1,2,3,4,5,6,7
if 8 in a:
    print("true")
if 6 in a:
    print("true")
if 7 in a:
    print("true")
if 8 not in a:
    print("false")


if 8 in a:
    print("true")
elif 7 in a:
    print("true")
elif 8 in a:
    print("true")
elif 2 in a:
    print("true")
else:
    print("false")

#nested if conditions
a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")

a=4
b=9
if a>b:
    print("less")
    if b>a:
        print("greater")

a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")

a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")

a=13
b=15
if a==b:
    print("true")
    if b>a:
        print("greater")
else:
    print("false")

a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")
else:
    print("not true")

a=20
b=25
if a!=b:
    print("true")
    if b==a:
        print("greater")
    elif a<b:
        print("less")
    else:
        print("false")

a=int(input())
b=int(input())
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("program ends")
    
