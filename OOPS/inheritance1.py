#inheritance

#single inheritance

class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()

#multiple inheritance


class father():
    def height(self):
        print("height is 5.5 inches")
class mother():
    def weight(self):
        print("weight is 60 kgs")
class kid():
    def dob(self):
        print("just born...")
a=father()
b=mother()
c=kid()
a.height()
b.weight()
c.dob()

class father():
    def height(self):
        print("height is 5.5 inches")
class mother():
    def weight(self):
        print("weight is 60 kgs")
class kid(father,mother):
    def dob(self):
        print("just born...")
a=kid()
a.weight()
a.height()
a.dob()

#multilevel inheritance

class grandparent():
    def land(self):
        print("10 acres")
class parent(grandparent):
    def house(self):
        print("100 sqft")
class child(parent):
    def car(self):
        print("BMW")
a=child()
a.land()
a.house()
a.car()

#hierarchical inheritance-hierarchical inheritance is where one parent class is inherited by multiple child classes

class employee():
   def company(self):
       print("codegnan it solutions")
class Trainer(employee):
    def teaching(self):
        print("trainer teach the code")
class Developer(employee):
    def code(self):
        print("developer develops the code")
a=Trainer()
a.teaching()
a.company()
b=Developer()
b.code()
b.company()
