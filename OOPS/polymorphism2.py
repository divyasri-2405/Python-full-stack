#polymorpishm

#operator overloading

'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(2))
print(a.__ge__(7))
print(a.__le__(10))
print(a.__eq__(2))

a=[1,2,3,4,5,6,7];b=[4,5,6,7,8,9,10]
print(a+b)
print(a.__getitem__(2))
print(b.__getitem__(5))

a="code";b="gnan"
print(a+b)
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())
print("divya".__add__("ch"))'''

#operator overriding

'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(6)
print(x+y)

class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=5
y=6
print(x+y)

#method overloading

class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
a=new()
a.sum()
a.sum(3,4,5)
a.sum(7,8)

#method overriding

class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()

class car():
    def Vehicle(self):
        print("car is running in 30 km/h")
class bike():
    def Vehicle(self):
        print("bike is running in 40 km/h")
a=car()
b=bike()
a.Vehicle()
b.Vehicle()'''

class car():
    def Vehicle(self):
        print("Thar")
class bike():
    def Vehicle(self):
        print("vespa")
a=car()
b=bike()
a.Vehicle()
b.Vehicle()
