#keyword and positional arguments
def details(id,name,mailid):
    id=10
    name="divya"
    mailid="divya123@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")

def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=30,name="sajad",mailid="sajad345@gmail.com")
details(id=50,name="adrayash",mailid="a@gmail.com")
details(40,"adrait","@gmail.com")
details("gh@gmail.com",35,"karishma")
details(mailid="v@gmail.com",id=20,name="varna")

#default arguments
def Grocery(item,price):
    print("the item is %s" %item)
    print("the price is %.2f" %price)
Grocery("rice",1000)

def grocery(item="sugar",price=1500):
    print("the item is %s" %item)
    print("the price is %.2f" %price)
grocery()

def grocery(item,price=2000):
    print("the item is %s" %item)
    print("the price is %.2f" %price)
grocery("dal")

def grocery(item='ghee',price):
    print("the item is %s" %item)
    print("the price is %.2f" %price)
grocery(2500)#error

#cake_name,price,qty
def bakery(cake_name,price,qty):
    print("The cake name is %s" %cake_name)
    print("the price is %.2f" %price)
    print("the qty is %d kg" %qty)
bakery("chocolate",1900,1)

def bakery(cake_name="butterstoch",price=1500,qty=2):
    print("the cake name is %s" %cake_name)
    print("the price is %.f" %price)
    print("the qty is %d kg" %qty)
bakery()

def bakery(cake_name,price=1770,qty=500):
    print("the cake name is %s" %cake_name)
    print("the price is %.2f" %price)
    print("the qty is %d g" %qty)
bakery("redvelvet")

def bakery(cake_name="pineapple",price,qty=750):
    print("the cake name is %s" %cake_name)
    print("the price is %.2f" %price)
    print("the qty is %d g" %qty)
bakery(2000)#error

def bakery(cake_name="black forest",price=1800,qty):
    print("the cake name is %s" %cake_name)
    print("the price is %.2f" %price)
    print("the qty is %d kg" %qty)
bakery(10) #error

#default arguments
a=[1,2,3,4,5,6,7]
print(a)
print(*a)

a=(1,2,3,4,5,6,7)
print(a)
print(*a)

a={1,2,3,4,5,6,7}
print(a)
print(*a)

a={"name":"divya","city":"Vja"}
print(a)
print(*a)

a,b,c=2,3,4,5,6,7,8
print(a)
print(b)
print(c) #error

a,b,c=2,3,5
print(a)
print(b)
print(c)

*a,b,c=2,3,4,5,6,7,8
print(*a)
print(b)
print(c)

a,*b,c=2,3,4,5,6,7,8
print(a)
print(*b)
print(c)

a,b,*c=2,3,4,5,6,7,8
print(a)
print(b)
print(*c)

a,b,c="codegnan"
print(a)
print(b)
print(c)

a,b,c="cod"
print(a)
print(b)
print(c)

a,b,*c="codegnan"
print(a)
print(b)
print(*c)

*a,b,c="codegnan"
print(*a)
print(b)
print(c)

a,*b,c="codegnan"
print(a)
print(*b)
print(c)



