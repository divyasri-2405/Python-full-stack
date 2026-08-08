#anonymous functions(nameless function)-anonymous functions are nameless function and we use a keyord called as "lambda" to create anonymous functions

#write a function to calculate 2*x+5 where x=5

def cal(x):
    return 2*x+5
print(cal(5))

def f(x):
    print(2*x+5)
f(5)

def f():
    x=int(input("value"))
    print(2*x+5)
f()

#syntax
#a=lambda arg:expr

a=lambda x:2*x+5
print(a(5))

a=int(input())
b=lambda x:2*x+5
print(b(a))

x=int(input())
y=int(input())
a=lambda x,y:x*y
print(a(x,y))

a=lambda x,y:x*y
print(a(4,5))

x,y=map(int,input().split())
a=lambda x,y:x*y
print(a(x,y))

#codegnan
#CODEGNAN

x=lambda a:a.upper()
print(x("codegnan"))

a="codegnan"
b=lambda a:a.upper()
print(b(a))

a=lambda a:a.upper()
print(a("codegnan"))

a=str(input())
x=lambda a:a.upper()
print(x(a))

a="python course"
#Python Course
b=lambda a:a.title()
print(b(a))

a=lambda a:a.title()
print(a("python course"))

a=input()
b=lambda a:a.title()
print(b(a))

a=lambda x:x.title()
print(a("python course"))

#firstname+lastname=fullname
firstname=str(input())
lastname=str(input())
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

firstname="hi"
lastname="namaste"
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

firstname,lastname=input().split()
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

#giving multiple inputs using generators and split

firstname,lastname=(x for x in input("enter firstname and lastname ").split(","))
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

firstname,lastname=[x for x in input("enter firstname and lastname ").split(",")]
fullname=lambda firstname,lastname:(firstname+" "+lastname).title()
print(fullname(firstname,lastname))

#filter()
a=[10,30,50,100,127,39,45,67,200]
for i in a:
    if i%2==0:
        print(i)

b=list(filter(lambda x:x%2==0,a))
print(b)

a=[[],(),set(),{}," ",None,5,8.9,"python",5+9j,True,False]
b=print(list(filter(None,a)))
print(b)

a=[[],(),set(),{}," ",5,8.9,"python",5+9j,True,False]
b=print(list(filter(None,a)))
print(b)

a=[]
print(type(a))

a=()
print(type(a))

a={}
print(type(a))

a=set()
print(type(a))










