#OOPS

#syntax

'''class classname():
    #attributes
    name="pooja"
    age=28
    place="vja"
    def function_name(method_name):
        print("statements...")
a=classname()
a.function_name()

#class declaration

class Details():
    name="pooja"
    age=28
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()

#object instantiation

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
b.display()'''

#object initialization

class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("kushal",22,"vja")
print(dir(a))
a.display()

