#while
'''a=10
while a>1:
    print(a)
while a<1:
    print(a)
while a>1:
    print(a)
    a=a-1
while a>=1:
    print(a)
    a=a-1
while a>3:
    a=a-1
    print(a)
while a>3:
    a=a-1
print(a)
a=30
while a>1:
    print(a)
    a+=1
a=10
while a>1:
    print(a)
    a-=1
a=1
while a<25:
    print(a)
    a+=1
while True:
    age=int(input("enter the age: "))
    if age>=18:
        print("eligible to vote")
    else:
        print("Not eligible to vote")

#range
#start-stop-step
for i in range(25):
    print(i)
for i in range(10,30):
    print(i)
#0,3,6,9,12,15,18,21,24,27
for i in range(0,30,3):
    print(i)
#5,10,15,20,25,30,35,40,45
for i in range(5,50,5):
    print(i)
#2,4,6,8,10,12,14,16,18
for i in range(2,20,2):
    print(i,end=" ")'''

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
    

