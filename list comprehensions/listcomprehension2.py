#list comprehension
a=['codegnan','python','course']
b=str(a)
print(b.upper())
for i in a:
    print(i.upper(),end=",")
b=[]
for i in a:
    b.append(i.upper())
print(b)

#syntax
#a=[expr for var in collection/range]
a=[i.upper() for i in a]
print(a)
a=['vja','hyd','vzg']
b=[i.title() for i in a]
print(b)
a=[1,2,3,5,6,8,12,13]
b=[(i**2) for i in a]
print(b)
b=[(i*i) for i in a]
print(b)
b=[pow(i,2) for i in a]
print(b)

#if-usage in list comprehension
for i in range(16):
    print(i)
b=[i for i in range(16)]
print(b)
b=[i for i in range(21) if i%2==0]
print(b)
b=[i for i in range(21) if i%2!=0]
print(b)
b=[i**2 for i in range(21) if i%2==0]
print(b)
b=[i*i for i in range(21) if i%2==0]
print(b)
b=[pow(i,2) for i in range(21) if i%2==0]
print(b)

a=["apple","banana","grapes","mango","kiwi","dragon","berry"]
b=[i for i in a if 'a' in i]
print(b)
b=[i for i in a if 'a' not in i]
print(b)

#if-else usage
a=[i**2 if i%2==0 else i*5 for i in range(31)]
print(a)

a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for  i in range(len(a))]
print(c)
c=[a[i]+b[i] for i in range(5)]
print(c)
