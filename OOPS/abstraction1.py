#abstraction-Hiding unnecessary information from user is abstraction

#abstract class-In abstract class have 1 or more abstract methods

#abstract method-The method declared without implementation is called abstract method

#abstraction

class A():
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
class A(ABC):
    @abstractmethod
    def method1(self):
        print("codegnan")
obj1=A()
obj1.method1()

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("python course")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data science")
    def method3(self):
        print("machine learning")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()


