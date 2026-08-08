#map()-each object from a collection and forms a new collection

#max(),min(),sum()
#max()-prints the maximum value from the collection
#min()-prints the minimum value from the collection
#sum()-prints the sum of values from the collection

print(max(8,4,6,0,1,27,9,5))

print(min(6,48,3,9,0,1,2,3,9,4))

print(sum([4,6,7,8,19,3]))

a=2,3,0,5,8,9,7,5,2,4,6,1
print(sum(a))

a=[2,5,7,8,10,12,14,16,20,25]
b=[1,3,5,7,9,11,15,17,21,24]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

a=[2,5,7,8,10,12,14,16,20,25,87]
b=[1,3,5,7,9,11,15,17,21,24]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

a=[2,5,7,8,10,12,14,16,20,25,94]
b=[1,3,5,7,9,11,15,17,21,24,94]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

a=input("data1")
b=input("data2")
print(a+b)

a,b=input("enter the names ").split(",")
print(a+b)

a,b=[x for x in input("enter the names").split(",")]
print(a+b)

a,b=map(str,input("enter the names").split(","))
print(a+b)

a=int(input())
b=int(input())
print(a+b)

a,b=[int(x) for x in input().split(",")]
print(a+b)

#a,b=int(input()).split(",")
#print(a+b)#error

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

a=list(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))

a=tuple(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))

a=set(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))

a=list(map(str,input("enter the values").split(",")))
print(a)
print(type(a))

a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)
