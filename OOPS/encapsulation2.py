#encapsulation

#public data

'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
a=child()
a.method1()
a.method2()

#_protecteddata

class parent():
    _protecteddata=1000
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__privatedata

class parent():
    __privatedata=10
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()
