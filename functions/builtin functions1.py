#built-in functions

print(dir())

print(dir("_builtins_"))

#fromkeys()

a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a)) #error

b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"divya")
print(c)

c["d"]="python"
print(c)

#eval()

while True:
    a=int(input("a value "))
    b=int(input("b value "))
    print(a+b)

while True:
    a=float(input('a value'))
    b=float(input('b value'))
    print(a+b)

while True:
    a=input("a value")
    b=input("b value")
    print(a+b)

while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)

#zip()-we can combine multiple collections into one collection

a=[10,20,30,40,50]
names=["khusal","manoj","harsha","sumanth","gopi"]
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
names=["khusal","manoj","harsha","sumanth","gopi"]
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

#enumerate()-we can give counter to the collection

names=["nikitha","taruni","siri","kalyani","prameela"]
for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names))
print(b)

b=list(enumerate(names,10))
print(b)

b=list(enumerate(names,100))
print(b)

#ASCII
#chr()
#ord()

print(chr(65))

print(chr(90))

#print(chr("A"))#error

print(ord("a"))

#print(ord(68))#error

print(ord("z"))

#alphabet order

for i in range(65,91):
    print(chr(i),end=" ")


for i in range(97,123):
    print(chr(i),end=" ")

a=input()
for i in a:
    print(i,"-",ord(i))

