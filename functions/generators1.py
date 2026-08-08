#generators
#no tuple comprehensions in above cases if we remove those braces and keep paranthesis when the outcome is generator

#generators
#[expr for var in collection/range]
a=[i for i in range(16)]
print(a)
print(type(a))

#(expr for var in collection/range)
a=(i for i in range(16))
print(a)
print(*a)
print(type(a))

b=list(a)
print(b)

print(tuple(a))
print(set(a))

#generators
# A generator is also a function which can be used as an iterator(loops) by producing group of values,where we can use "yield" keyword
#yield vs return
#return will terminate the function where as yield can pass the function and go on with every successive iteration

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))

#yield-generator-print(*)

a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))

a,b=[int(i) for i in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        yield a
print(*check(a,b))

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
        return a
print(*check(a,b))


a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        yield a
        return a
print(*check(a,b))

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
    return a
print(*check(a,b))

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        yield a
    return a
print(*check(a,b))

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
    return a
print(check(a,b))

#* is not used in return unless it returns multiple values

#yield vs return

def mygen():
    return "vja"
    return "hyd"
    return "vzg"
print(*mygen())

def mygen():
    return "vzg","vja","hyd"
print(*mygen())

def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
#print(next(d))#stop iteration
