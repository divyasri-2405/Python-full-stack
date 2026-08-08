#functions

full_name-snake
_full_name-pascal
full
a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("th product is",a*b)

def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)

def calci(a,b):
    print("the division is",a/b)
    print("the power is",a**b)
    print("the modulo is",a%b)
calci(10,20)
calci(8,10)
calci(9,3)
calci(2,8)
calci(3,4)

def add(a,b):
    print(a+b)
add(8,9)

def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
cal()

while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    cal()

def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()

def mul(a,b):
    print(a*b)
mul(2,9)

def mul(a,b):
    return a*b
mul(2,9)

def mul(a,b):
    return a*b
print(mul(2,3))

#print vs return
def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(3,4)

def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(add(3,4))

def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return d
    return e
print(add(3,4))

def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return e
print(add(3,4))

def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(add(3,4))

#splitbill()
def splitbill():
    n=int(input("number of persons"))
    bill=int(input("total bill"))
    average=bill/n
    return average
print(splitbill())

def splitbill():
    n=int(input("number of persons"))
    bill=int(input("total bill"))
    average=bill/n
    print(f"The each will pay {average}")
splitbill()

def splitbill():
    n=int(input("number of persons"))
    bill=int(input("total bill"))
    average=bill/n
    print("The each will pay",average)
splitbill()

def splitbill():
    n=int(input("number of persons"))
    bill=int(input("total bill"))
    average=bill/n
    print("The each will pay {}".format(average))
splitbill()

def splitbill():
    n=int(input("number of persons"))
    bill=int(input("total bill"))
    average=bill//n
    print("The each will pay {}".format(average))
splitbill()

def splitbill():
    a=int(input("total members"))
    b=int(input("total amount"))
    c=b//a
    print("perhead bill is {}".format(c))
    print(f"perhead bill is {c}")
splitbill()

def splitbill():
    a=int(input("total members"))
    b=int(input("total amount"))
    print("perhead bill is {}".format(b//a))
    print(f"perhead bill is {b//a}")
splitbill()

#options
def options():
    a=int(input())
    b=int(input())
    op=int(input('enter a option
1.add
2.sub
3.multi'))
    if op==1:
        print(a+b)
    elif op==2:
        print(a-b)
    elif op==3:
        print(a*b)
options()

while True:
    def options():
        a=int(input())
        b=int(input())
        op=int(input('enter a option
    1.add
    2.sub
    3.multi'))
        if op==1:
            print(a+b)
        elif op==2:
            print(a-b)
        elif op==3:
            print(a*b)
    options()

def add():
    print(a+b)
def sub():
    print(a-b)
def multi():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input('''choose the option
1.add
2.sub
3.multi'''))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        multi()
    
    

