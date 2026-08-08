#functions
a=10;b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100;b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(200,100)
calculate(1000,2000)

def calci(a,b):
    print("the divison is",a/b)
    print("the power is",a**b)
    print("the modulo is",a%b)
calci(8,9)
calci(90,50)
calci(57,20)

def add(a,b):
    print(a+b)
add(5,6)

def cal():
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a+b)
cal()

while True:
    def cal():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        print(a+b)
    cal()'

def fullname():
    first_name=input("enter first name")
    last_name=input("enter last name")
    print((first_name+" "+last_name).title())
fullname()

def mul(a,b):
    print(a*b)
mul(9,7)

def mul(a,b):
    return a*b
mul(9,8)

def mul(a,b):
    return a*b
print(mul(9,7))

#print vs return
def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
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

#splitbill
def splitbill():
    n=int(input("number of persons"))
    bill=int(input("total bill"))
    average=bill/n
    print("The each will pay",average)
    print("The each will pay {}".format(average))
    print(f"The each will pay {average}")
splitbill()

def splitbill():
    n=int(input("number of persons"))
    bill=int(input("total bill"))
    print("The each will pay {}".format(bill//n))
    print(f"The each will pay {bill//n}")
splitbill()

#options
def options():
    a=int(input())
    b=int(input())
    op=int(input("""enter a option
1.add
2.sub
3.multi"""))
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
        op=int(input("""enter a option
    1.add
    2.sub
    3.multi"""))
        if op==1:
            print(a+b)
        elif op==2:
            print(a-b)
        elif op==3:
            print(a*b)
    options()

def add():
    print(a+b)
def diff():
    print(a-b)
def multi():
    print(a*b)
while True:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    op=int(input("""choose a option
1.add
2.sub
3.multi"""))
    if op==1:
        add()
    elif op==2:
        diff()
    elif op==3:
        multi()
