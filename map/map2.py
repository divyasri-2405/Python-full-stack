#map()
'''print(max(2,6,1,9,34,8,5))

print(min(2,6,1,9,34,8,5))

print(sum([2,6,1,9,34,8,5]))

a=2,6,1,9,34,8,5
print(sum(a))

a=[2,5,7,8,10,12,14,16,20,25]
b=[1,3,5,7,9,11,15,17,21,24]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

a=[2,5,7,8,10,12,14,16,20,25,98]
b=[1,3,5,7,9,11,15,17,21,24]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

a=[2,5,7,8,10,12,14,16,20,25,30]
b=[1,3,5,7,9,11,15,17,21,24,30]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

a=input()
b=input()
print(a+b)

a,b=input("enter the names").split(",")
print(a+b)

a,b=[x for x in input("enter the names").split(",")]
print(a+b)

a,b=map(str,input("enter the names").split(","))
print(a+b)

a=int(input())
b=int(input())
print(a+b)

a,b=int(input()).split(',')
print(a+b)#error'

a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)

a,b=map(int,input("enter the values").split(","))
print(a+b)

a=list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))

a=tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))

a=set(map(int,input("enter the values").split(",")))
print(a)
print(type(a))

a=list(map(str,input("enter the values").split(",")))
print(a)
print(type(a))

a=list(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))

a=tuple(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))

a=set(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))'''

a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)


