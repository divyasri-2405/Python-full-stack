#keyword and positional arguments

def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@codegnan.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid") #giving keywords and "id" as positional arguments

def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="manoj",mailid="m@gmail.com")
Details(id=30,name="harsha",mailid="h@gmail.com") #giving values same as arguments with keywords
Details(40,"trinadh","t@gmail.com") #giving values same as arguments
Details("d@gmail.com",50,"sai") #giving values not same as arguments and it will not print same as arguments
Details(mailid="g@gmail.com",id=60,name="gopi") #giving values not same as arguments but with keywords and in different positions and it will print correct order

#default arguments

def Grocery(item,price): #giving argument values at last function
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)

def Grocery(item="rice",price=1500): #both arguments are initialized here
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()

def Grocery(item,price=200): #first argument can be empty
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dal")

def Grocery(item='ghee',price):#non def arg follows def else
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)

#cake_name,price,qty

def bakery(cake_name,price,qty):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg" %qty)
bakery("Chocolate",900,10 )

def bakery(cake_name="butterstoch",price=300,qty=1):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg" %qty)
bakery()

def bakery(cake_name,price=570,qty=500):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d g" %qty)
bakery("redvelvet")

def bakery(cake_name="pineapple",price,qty=2):
     print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg" %qty)
bakery("1500") #error

def bakery(cake_name="black forest",price=350,qty):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg" %qty)
bakery(3) #error

#* arguments(* is used to unpack the elements)

a=[1,2,3,4,5,6,7]
print(a)
print(*a)

a=(2,3,4,5,6,7)
print(a)
print(*a)

a={2,3,4,5,6,7}
print(a)
print(*a)

b={"name":"pooja","city":"vja"}
print(b)
print(*b) #only keywords are printed

c="python"
print(c)
print(*c)

a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c) #error

a,b,c=2,3,4
print(a)
print(b)
print(c)

*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)

a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)

a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)

*a,b,*c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(*c) #multiple expression #error

a,b,c="codegnan"
print(a)
print(b)
print(c) #error

a,b,c="cod"
print(a)
print(b)
print(c)

a,b,*c="codegnan"
print(a)
print(b)
print(*c)









