#while loop-continuous iteration
a=10
while a>1:
    print(a)

a=10
while a<1:
    print(a)

a=10
while a>1:
    print(a)
    a=a-1

a=10
while a>=1:
    print(a)
    a=a-1

a=20
while a>3:
    print(a)
    a=a-1

a=20
while a>3:
    a=a-1
    print(a)

a=20
while a>3:
    a=a-1
print(a)

a=40
while a>5:
    a=a-1
print(a)

a=30
while a>1:
    print(a)
    a+=1

a=10
while a>2:
    print(a)
    a-=1

a=30
while a>1:
    print(a)
    a-=1

a=1
while a<25:
    print(a)
    a+=1

while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")

while True:
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

#range()-The range function returns a sequence of number,starting from 0 by default and increments by 1 by 1 and stops before a specified number
#start-stop-step
for i in range(20):
    print(i)

for i in range(13,35):
    print(i)'

#0,3,6,9,12,15,18,21,24,27
for i in range(0,30,3):
    print(i)

#5,10,15,20,25,30,35,40,45
for i in range(5,50,5):
    print(i)

#2,4,6,8,10,12,14,16,18
for i in range(2,20,2):
    print(i)

#0,3,6,9,12,15,18,21,24,27
for i in range(0,30,3):
    print(i,end=" ")

#5,10,15,20,25,30,35,40,45
for i in range(5,50,5):
    print(i,end=" ")
    
#2,4,6,8,10,12,14,16,18
for i in range(2,20,2):
    print(i,end=" ")

#0,3,6,9,12,15,18,21,24,27
for i in range(0,30,3):
    print(i,end=",")

#marks
while True:
    marks=int(input())
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(50,71):
        print("Grade D")
    else:
        print("Fail")

