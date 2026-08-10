#abstraction

'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()

class A():
    def method1(self):
        print("python")
obj1=A()
obj1.method1()

from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()

from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print("data")
obj1=A()
obj1.method1()

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("codegnan")
obj1=A()
obj1.method1()'''

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("python")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data science")
    def method3(self):
        print("machine learning")
a=B()
a.method1()
a.method2()
a.method3()
