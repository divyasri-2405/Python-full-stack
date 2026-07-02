Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="divya sri"
lname="motamarri"
print(fname+lname)
divya srimotamarri
print(fname+" "+lname)
divya sri motamarri
print(fname.capitalize()+" "+lname.capitalize())
Divya sri Motamarri
print((fname+" "+lname).capitalize)
<built-in method capitalize of str object at 0x0000029FE3DABC70>
print(fname.title()+" "+lname.title())
Divya Sri Motamarri
print((fname+" "+lname).title)
<built-in method title of str object at 0x0000029FE3DABA70>
print((fname+" "+lname).capitalize())
Divya sri motamarri
print((fname+" "+lname).title())
Divya Sri Motamarri
#formatting
a=5;b=6
print(a+b)
11
print("the sum is",a+b)
the sum is 11
x="vja"
print("city is",x)
city is vja
y="name"
print(1 ,y)
1 name
print("1",y)
1 name
#format method
a=motu
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a=motu
NameError: name 'motu' is not defined
a="motu"
b="patlu"
print("hello",a+b)
hello motupatlu
print("hello {} {}",a+b)
hello {} {} motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {}  {} ".format(a,b))
hello motu  patlu 
print("hello  {}    hello  {} ".format(a,b))
hello  motu    hello  patlu 
a="sita";b="ram"
print(f"hello {a} {b}")
hello sita ram
print(f"hello   {a}       {b}")
hello   sita       ram
print(f"hello  {a}  hello {b}")
hello  sita  hello ram
c=15;d=5
print("the product is {} {}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print("the product is {} {}".format(a*b))
TypeError: can't multiply sequence by non-int of type 'str'
print("the product is {} {}"a*b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("the product is {} {}",a*b)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print("the product is {} {}",a*b)
TypeError: can't multiply sequence by non-int of type 'str'
>>> c=15;d=5;
>>> product=a*b
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    product=a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> product=c*d
>>> print(product)
75
>>> print("the product is {}",product)
the product is {} 75
>>> print("the product is ",product)
the product is  75
>>> print("the product is".format(product))
the product is
>>> print("the product is {}".format(product))
the product is 75
>>> print("the product is {product}")
the product is {product}
>>> print(f"the product is {product}")
the product is 75
>>> print("the product is {}".format(c*d))
the product is 75
>>> print(f"the product is{product}")
the product is75
>>> print(f"the product is {product}")
the product is 75
>>> a=4
>>> b=5
>>> c=a*b
>>> print(c)
20
>>> print("the product is".format(c))
the product is
>>> print("the product is {} ".format(c))
the product is 20 
>>> print(f"the product is {c}")
the product is 20
>>> print("the product is {} ".format(a*b))
the product is 20
>>> print("the product is {a*b}")
the product is {a*b}
