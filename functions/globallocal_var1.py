#global and local variables
#variables inside and outside the function is called global and local variables
#A variable is defined above the function and is accessible to entire global space is called global variables
#A Variable is inside the function is called local variable

#global and local variables
#first case of global variables
a=4
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)

#second case of global and local variable
a=2
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)

#third case of both global and local variables
a=6
def check3():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=13#local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)

#usage of global keyword
#when user wants to access the global variable inside the function directly and carry forward the updated value even outside the function then we need to use the global keyword

a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("update vlaue is",a)
    #global b
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)
