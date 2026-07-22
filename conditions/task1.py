#voting
age=int(input("enter the age:"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")

#even or odd
num=int(input("enter the number "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#leap year
year=int(input("enter the leap year "))
if year%4==0:
    print("leap year")
else:
    print("not leap year")

#guest code
name=str(input())
if name=="Pooja":
    print("Welcome Pooja")
else:
    print("Welcome Guest")
name=str(input())
if name=="pooja":
    print("Welcome"+" "+name)
else:
    print("Welcome Guest")
name=input("enter the name")
if name=="pooja":
    print("Welcome",name)
else:
    print("welcome guest")
name=input("enter the name").lower()
if name=="pooja":
    print("welcome",name)
else:
    print("welcome guest")

names=['divya','kavya','vaishu','girija','kumar']
a=input("enter a name ")
if a in names:
    print("Welcome",a)
else:
    print("Welcome guest")

#vowels
vowels=['a','e','i','o','u']
name=input("enter a letter ")
if name in vowels:
    print("it is vowel")
else:
    print("it is not vowel")
vowels=['a','e','i','o','u']
name=input("enter a letter ").lower()
if name in vowels:
    print("it is vowel")
else:
    print("it is not vowel")

#social_media_login
username=input("enter a username ")
password=int(input("enter a password "))
if username=="divya":
    if password==1234:
        print("login successful")
    else:
        print("incorrect password")
else:
    print("invalid username")

a="sajad"
b=1234
username=input("enter the username")
password=int(input("enter the password"))
if username==a:
    if password==b:
        print("login successful")
    else:
        print("incorrect password")
else:
    print("invalid username")

username=input("enter the username")
password=input("enter the password")
if username==username and password==password:
    print("login successful")
else:
    print("Invalid credentials")

username=input("enter the username")
password=input("enter the password")
if username=="divyasri" and password=="sajad@54321":
    print("login successful")
else:
    print("Invalid credentials")

age=int(input("enter the age"))
marks=int(input("enter the marks"))
attendance=int(input("enter the percentage"))
if age>=18:
    print("age eligible")
if marks>=80:
    print("eligible for vote")
if attendance>=70:
    print("allow to exams")
