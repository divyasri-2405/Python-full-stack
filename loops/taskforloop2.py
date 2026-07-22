#bakery
cake_price=int(input("enter the cake  price "))
if cake_price==1200:
    print("red velvet cake")
elif cake_price==1000:
    print("almond cake")
elif cake_price==800:
    print("chocolate cake")
elif cake_price==600:
    print("butter scotch cake")
else:
    print("cake is not available")

#pizza
pizza_name=input("Enter the pizza name: ")
if pizza_name=="bbq pizza":
    print(800)
elif pizza_name=="crispy chicken pizza":
    print(600)
elif pizza_name=="panner pizza":
    print(400)
elif pizza_name=="corn pizza":
    print(200)
else:
    print(150)

pizza_name=input("Enter the pizza name: ")
if pizza_name=="bbq pizza":
    print(800)
elif pizza_name=="crispy chicken pizza":
    print(600)
elif pizza_name=="panner pizza":
    print(400)
elif pizza_name=="corn pizza":
    print(200)
elif pizza_name=="french fries and coke":
    print(150)

#for loop
a=[1,2,3,4,5]
for i in a:
    print(i)

for i in a:
    print(a)

for i in a:
    print(i,end=" ")

a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))

for i in a:
    print(i)
    print(type(a))
    print(type(i))

a=(5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))

a={5,6,7,8}
for i in a:
    print(i)
print(type(a))
print(type(i))

b={"year":2026,"Month":"July","date":9}
for i in b:
    print(i)
    print(type(b))
    print(type(i))
for i in b.keys():
    print(i)
    print(type(b))
    print(type(i))
for i in b.values():
    print(i)
    print(type(b))
    print(type(i))
for i in b.items():
    print(i)
    print(type(b))
    print(type(i))

a="codegnan"
for i in a:
    print(i)

b=[4.5,5.6,6.7]
for i in b:
    print(i)
    print(type(b))
    print(type(i))

b=['c++','java','python']
for i in b:
    print(i)
    print(type(b))
    print(type(i))

b=[4+8j,9+7j]
for i in b:
    print(i)
    print(type(b))
    print(type(i))

b=[True,False]
for i in b:
    print(i)
    print(type(b))
    print(type(i))

a=["apple","mango","banana"]
b=[]
for i in a:
    b.append(i.upper())
print(b)

a=[1,3,5,7,9,'code']
a.extend('code')
print(a)

a=[1,3,5,7]
a.extend('code')
print(a)
