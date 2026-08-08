#built-in functions

'''print(dir())

print(dir("_builtins_"))

#fromkeys()

a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))

b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"divya")
print(c)

c["d"]="python"
print(c)'''

#eval()

'''while True:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a+b)

while True:
    a=float(input("enter a value"))
    b=float(input("enter b value"))
    print(a+b)

while True:
    a=input("enter a value")
    b=input("enter b value")
    print(a+b)

while True:
    a=eval(input("enter a value"))
    b=eval(input("enter b value"))
    print(a+b)

#zip()

a=[10,20,30,40,50]
names=["divya","kavya","vaishnavi","girija","kumar"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)

a=[10,20,30,40,50,60]
names=["divya","kavya","vaishnavi","girija","kumar"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''

names=["divya","sajad","adryash","adrait","varna"]
'''for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names))
print(b)

b=list(enumerate(names,10))
print(b)

b=list(enumerate(names,100))
print(b)

#ASCII
#chr
#ord

print(chr(65))

#print(chr("A"))

print(chr(56))

print(chr(90))

print(chr(123))

print(ord('A'))

#print(ord(97))

print(ord('Z'))

print(ord('a'))

print(ord('z'))

print(ord("*"))

#alphabet order

for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

a=input()
for i in a:
    print(i,"-",ord(i))






