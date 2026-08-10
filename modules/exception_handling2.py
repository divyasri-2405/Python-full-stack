#exception handling

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends...")

while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends...")

#regex

a="codegnan is in vijayawada"
print(a)

a="codegnan\nis\tin\nvijayawada"
print(a)

#sequence characters

#compile()

import re
a="mat cat cap maths money cash code cup dog donkey must"
b=re.compile(r"m\w\w\w\w")
print(b)

#search()

c=b.search(a)
print(c)

b=re.search(r"m\w+",a)
print(b)

#findall()

c=re.findall(r"c\w+",a)
print(c)

c=re.findall(r"c\w+",a)
print(*c)

c=re.findall(r"d\w+",a)
print(*c)

#split()

d=re.split("m",a)
print(d)

d=re.split(r"m",a)
print(d)

e=re.split(r"\s",a)
print(e)

e=re.split(r"\S",a)
print(e)

#sub()

f=re.sub("m","a",a)
print(f)

#task

import re
a="year 2026 month 8 day 25"
b=re.findall(r"\d+",a)
print(b)

b=re.findall(r"\D+",a)
print(b)'''

import re
e="code mon monkey"
'''f=re.findall(r"\d\w",e)
print(f)'''

f=re.findall(r"\w+",e)
print(f)

q=re.findall(r"\bco\w+",e)
print(q)
