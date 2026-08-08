#anonymous function

'''def cal(x):
    return 2*x+5
print(cal(5))

def f(x):
    print(2*x+5)
f(5)

def f():
    x=int(input("value"))
    print(2*x+5)
f()

#a=lambda arg:expr

a=lambda x:2*x+5
print(a(5))

a=int(input())
b=lambda x:2*x+5
print(b(a))

a=lambda x,y:x*y
print(a(4,5))

x=int(input())
y=int(input())
a=lambda x,y:x*y
print(a(x,y))

x,y=map(int,input().split())
a=lambda x,y:x*y
print(a(x,y))

x=lambda a:a.upper()
print(x("codegnan"))

a=lambda a:a.upper()
print(a("codegnan"))

a=str(input())
x=lambda a:a.upper()
print(x(a))

a="python course"
b=lambda a:a.title()
print(b(a))

b=lambda x:x.title()
print(b("python course"))

a=lambda a:a.title()
print(a("python course"))

a=input()
b=lambda a:a.title()
print(b(a))

firstname=str(input())
lastname=str(input())
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

firstname="hi"
lastname="namaste"
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname("hello","hi"))

firstname,lastname=input().split()
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

firstname,lastname=(x for x in input("enter firstname and lastname").split(','))
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

firstname,lastname=[x for x in input("enter firstname and lastname").split()]
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))'''

#filter()
a=[10,30,50,100,127,39,45,67,200]
'''for i in a:
    if i%2==0:
        print(i)

b=list(filter(lambda x:x%2==0,a))
print(b)

a=[[],(),set(),{},None," ",5,5.8,"python",9+8j,True,False]
b=list(filter(None,a))
print(b)

a=[[],(),set(),{}," ",5,8.7,"python",9+8j,True,False]
b=list(filter(None,a))
print(b)'''

a=[]
print(type(a))

a=()
print(type(a))

a=set()
print(type(a))

a={}
print(type(a))
