#inheritance

#single inheritance

'''class RBI():
    cash=100000
    def available_cash(cls):
        print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
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
c=kid()
c.height()
c.weight()
c.dob()

#mulitlevel inheritance

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
a.car()'''

#hierarchical inheritance

class employee():
    def company(self):
        print("Codegnan IT solutions")
class Trainer(employee):
    def teaching(self):
        print("trainer teaching the code")
class Developer(employee):
    def code(self):
        print("developer develops the code")
a=Trainer()
a.teaching()
a.company()
b=Developer()
b.code()
b.company()


