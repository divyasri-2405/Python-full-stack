'''a=[i for i in range(16)]
print(a)
print(type(a))

a=(i for i in range(16))
print(a)
print(*a)
print(type(a))

b=list(a)
print(b)

print(tuple(a))
print(set(a))

#generators

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        yield a
print(*check(a,b))

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
    return a
print(*check(a,b))

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
        return a
print(*check(a,b))

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        yield a
    return a
print(*check(a,b))

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        yield a
        return a
print(*check(a,b))

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        a=a+1
    return a
print(check(a,b))

#yield vs return

def mygen():
    return "vja"
    return "hyd"
    return "vgz"
print(*mygen())

def mygen():
    return "vja","vzg","hyd"
print(*mygen())'''

def mygen():
    yield "vja"
    yield "vzg"
    yield "hyd"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
#print(next(d)) #stop iteration




