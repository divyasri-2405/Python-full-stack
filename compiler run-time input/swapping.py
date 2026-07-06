#swapping of two variables
a=10
b=20
a=b
print(a)

#using two variables
a=10
b=40
a,b=b,a
print("a value is",a)
print("b value is",b)

#using temporary variable
a=12
b=13
temp=a
a=b
b=temp
print("a value is",a)
print("b value is",b)

#using arthimetic operators
a=10
b=22
a=a+b
b=a-b
a=a-b
print("a value is",a)
print("b value is",b)

#using %percentage value
a=22
b=55
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))

a=33.45
b=6.78
a=a+b
b=a-b
a=a-b
print("after swapping a=%f,b=%f" %(a,b))

a=44.98
b=9.4
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f" %(a,b))

a=float(input())
b=float(input())
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f" %(a,b))

a=input()
b=input()
a,b=b,a
print("after swapping a=%s,b=%s" %(a,b))

