'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name"),int(input("age")),input("place"))
print(dir(a))

class Details():
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()

class employee():
    def __init__(self):
        self.name="divya"
        self._mailid="divya12@gmail.com"
        self.__salary=10000
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee__salary)'''

class employee1():
    def __init__(self):
        self.name="sajad"
        self._mailid="sajad34@gmail.com"
        self.__salary=20000
class employee2():
    def __init__(self):
        self.name="mds"
        self._mailid="mds12@gmail.com"
        self.__salary=30000
class employee3():
    def __init__(self):
        self.name="mlsk"
        self._mailid="mlsk34@gmsil.com"
        self.__salary=400000
a=employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee1__salary)
b=employee2()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._employee2__salary)
c=employee3()
print(dir(c))
print(c.name)
print(c._mailid)
print(c._employee3__salary)
