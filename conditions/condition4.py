#conditions
#if-elif-else:
#if-elif-else using comparison operators
a=4;b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")
if a==b:
    print("less")
elif a>=b:
    print("true")
else:
    print("greater")

#if-elif-else using logical operator
a=4;b=6
if a<b and b>a:
    print("true")
elif a>b and b<a:
    print("false")
if a>=b and b<=a:
    print("less")
elif a<=b and b>=a:
    print("greater")
else:
    print("true")
if a==b and a!=b:
    print("less")
elif a>=b and b<=a:
    print("greater")
else:
    print("true")
if a<b or b>a:
    print("true")
elif a>b or b<a:
    print("false")
if a<=b or b>=a:
    print("less")
elif a>=b or a!=b:
    print("high")
else:
    print("true")
if a==b or a>=b:
    print("true")
elif a<=b or b<=a:
    print("false")
else:
    print("less")
if not a>b:
    print("less")
elif not a<b:
    print("more")
if not a<=b and b>=a:
    print("less")
elif not a>=b or b<=a:
    print("more")
else:
    print("high")

#if-elif-else using identify operators
a=5
if type(a) is int:
    print("true")
elif type(a) is not int:
    print("false")
a=5.6
if type(a) is float:
    print("true")
elif type(a) is not float:
    print("false")
else:
    print("less")
a="hi"
if type(a) is str:
    print("true")
elif type(a) is not int:
    print("false")
else:
    print("less")
a=4+8j
if type(a) is complex:
    print("true")
elif type(a) is not complex:
    print("false")
else:
    print("less")
a=True
if type(a) is bool:
    print("true")
elif type(a) is not bool:
    print("false")
else:
    print("less")

#if-elif-else using membership operators
a=1,2,3,4,5,6,7,8
b=int(input())
if 8 in a:
    print("true")
elif 8 not in a:
    print("false")
if b in a:
    print("true")
elif b not in a:
    print("false")
else:
    print("less")

#multiple-if conditions
#mulitple-if and elif conditions using comparison operators
a=20;b=40
if a<b:
    print("less")
if b>a:
    print("high")
if a!=b:
    print("true")
if a<=b:
    print("less")
if b>=a:
    print("high")
if a==b:
    print("true")
else:
    print("false")
if a<b:
    print("less")
elif b>a:
    print("high")
elif a!=b:
  print("true")
elif a<=b:
    print("false")
if a>=b:
    print("less")
elif b<=a:
    print("high")
elif a!=b:
    print("true")
elif a==b:
    print("more")
else:
    print("false")
    
#multiple-if and elif conditions using logical operators
a=40;b=90
if a<b and b>a:
    print("true")
if a<=b or b>=a:
    print("false")
if not a==b and b!=a:
    print("less")
if a<b or b>a:
    print("true")
if a<=b and b>=a:
    print("false")
if not a<=b and b>=a:
    print("less")
else:
    print("high")
if a<b and b>a:
    print("true")
elif a<=b or b>a:
    print("false")
elif not a<=b and b<=a:
    print("high")
if a<b or b>a:
    print("true")
elif a<=b and b>=a:
    print("false")
elif a==b or a!=b:
    print("high")
else:
    print("low")

#multiple-if and elif conditions using membership operators
a=1,2,3,4,5,6,7,8
b=int(input())
if 8 in a:
    print("true")
if 6 in a:
    print("high")
if 9 in a:
    print("low")
if 10 not in a:
    print("false")
if b in a:
    print("true")
if 4 in a:
    print("high")
if 8 not in a:
    print("low")
else:
    print("false")
if 5 in a:
    print("true")
elif 8 in a:
    print("high")
elif 6 not in a:
    print("low")
if 10 in a:
    print("true")
elif 2 in a:
    print("high")
elif 6 not in a:
    print("low")
else:
    print("false")

#multiple-if and elif conditions using identify operators
a=5
if type(a) is int:
    print("true")
if type(a) is str:
    print("less")
if type(a) is not float:
    print("high")
a=7.8
if type(a) is float:
    print("true")
if type(a) is str:
    print('less')
if type(a) is not complex:
    print('high')
if type(a) is not float:
    print('more')
else:
    print("false")
a='hi'
if type(a) is str:
    print("true")
elif type(a) is not str:
    print("high")
elif type(a) is complex:
    print("low")
a=4+8j
if type(a) is bool:
    print("true")
elif type(a) is not str:
    print("high")
elif type(a) is complex:
    print("low")
else:
    print("false")

#nested-if conditions
a=4;b=9
if a<b:
    print("true")
    if b>a:
        print('false')
if a>b:
    print('true')
    if b>a:
        print('false')
a=7;b=11
if a!=b:
    print("less")
    if b==a:
        print("high")
if a!=b:
    print("less")
    if b==a:
        print("high")
    else:
        print("false")
if a==b:
    print("less")
    if a<b:
        print("true")
else:
    print("false")
if a!=b:
    print("less")
    if b==a:
        print("high")
    else:
        print("true")
else:
    print("false")
if a!=b:
    print("true")
    if a>b:
        print("more")
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
