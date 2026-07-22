#break
a=10
while a>1:
    print(a)
    a=a-1
a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break
a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)
for i in range(20):
    if i==14:
        break
    print(i)
a=10;b=20;c=30
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")
a="python"
for i in a:
    if i=="h":
        break
    print(i)
#continue
a=20
while a>5:
    print(a)
    a=a-1
a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue
a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)
for i in range(20):
    if i==12:
        continue
    print(i)
a="python"
for i in a:
    if i=="t":
        continue
    print(i)
#pass
a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        pass
for i in range(40):
    if i==10:
        pass
    print(i)

    

    
