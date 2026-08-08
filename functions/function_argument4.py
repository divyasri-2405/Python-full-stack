#variable length arguments
def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[1,2,3,4,5,6,7]
check(*b)
c=(1,2,3,4,5,6,7,8)
check(*c)
d={1,2,3,4,5,6,7}
check(*d)
e={"name":"divya","place":"vja"}
check(*e)

def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5)
check1(2.3,4.5,6.7,8.9,9.1)
check1(3,4,6,7,9,10,7.8,9.1,2.3,5.7,1.4,"python")

#**(kwargs)
def check2(**a):
    print(a)
    print(type(a))
check2()
details={"name":["sweety","beauty","hearty"],
         "marks":[90,50,80],
         "status":["p","a","p"]}
check2(**details)

def check3(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check3()
details={"name":["sweety","cuty","Hearty"],
         "marks":[50,70,90],
         "status":["p","a","p"]}
check3(**details)

#both * and ** usage
def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
final()
data=(2,3,4,5,6,7,8.5,9.6)
print(data)
details={"year":[2024,2025,2026],
         "month":["june","july","august"]}
final(**details)
final(*data,**details)
