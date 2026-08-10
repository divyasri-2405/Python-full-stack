#inheritance

#hybrid inheritance

'''class person():
    def details(self):
        print("I am divya")
class Trainer(person):
    def Teaching(self):
        print("Trainer teach the subject")
class Student(person):
    def study(self):
        print("preparing for exams")
class program_manager(Trainer,Student):
    def Manager(self):
        print("assign the classes")
a=program_manager()
a.details()
a.Teaching()
a.study()'''

#super()

class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("divya",21)
print(dir(a))
print(a.name)
print(a.age)
