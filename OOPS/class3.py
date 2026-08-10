#difference between _ and __

#when user wants to create a variable with double leading underscore (or) __ our python interpreter treats it as a special variable to avoid name conflicts with methods and inner classes

class employee1():
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@codegnan.com"
        self.__salary=10000 #private variable
class employee2():
    def __init__(self):
        self.name="arya"
        self._mailid="arya@codegnan.com"
        self.__salary=20000 #private variable
class employee3():
    def __init__(self):
        self.name="ramana"
        self._mailid="ramana@codegnan.com"
        self.__salary=30000 #private variable
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

class employee1():
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@codegnan.com"
        self.__salary=10000 #private variable
a=employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._employee1__salary)
