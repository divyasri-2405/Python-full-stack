#global and local variables
#first case of global variables
'''a=4
def check1():
    print("Inside value is",a)
check1()
print("Outside value is",a)

#second case of global and local variable
a=2
def check2():
    a=5
    a=a**2
    print("Inside value is",a)
check2()
print("Outside value is",a)

#third case of global and local variables
a=3
def check3():
    a=5
    print("Inside the value",a)
    a=10
    print("Updated value is",a+5)
    b=13
    print("b value is",b)
check3()
print("a value is",a)
print("b value is",b)

#usage of global keyword
a=4
def check4():
    global a,b
    print("inside the value",a)
    a=15
    print("Updated value is",a)
    b=13
    b=b+a
    print("b value is",b)
check4()
print("a value is",a)
print("b value is",b)'''

a=5
def final():
    global a
    print("inside the value",a)
    a=10
    print("Update value is",a)
    global b
    b=19
    b=b+a
    print("value of b",b)
final()
print("a value is",a)
print("b value is",b)



