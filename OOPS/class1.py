#OOPS
#syntax

class classname():
    #attributes
    name="Pooja"
    age=28
    place="vja"
    def function_name(method_name):
        print("statements........")
a=classname()
a.function_name()

#class declaration-declaring the class

class Details():
    name="pooja"
    age=28
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()

#object instantiation-instantly creating objects

class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("sumanth",21,"vja")
a.display()
b=Details()
b.data("manoj",22,"vja")
b.display()

#object initialization-starting
#here we use constructor while using a constructor we does not need function and also pass the attributes value inside the class

class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("kushal",22,"vja")
print(dir(a))
a.display()

class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
name=input()
age=int(input())
place=input()
a=Details(name,age,place)
print(dir(a))
a.display()

class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()

class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()



