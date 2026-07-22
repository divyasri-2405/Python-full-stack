#difference between break,continue and pass
#break-break is used to terminate the entire loop
#continue-continue statement is used to skips the current iteration and rest of the code will continue
#pass-A pass is a null statement it does nothing but syntatically we need.

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
    if i==13:
        break
    print(i)

a="python"
if a=="h":
    break
print(a)#error

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

for i in range(15):
    if i==7:
        continue
    print(i)

a="python"
for i in a:
    if i=="y":
        continue
    print(i)

#pass-placeholder
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


    



