#voting
age=int(input("enter the age"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")
#even or odd
num=int(input("enter the input "))
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
if name=="divya":
    print("welcome divya")
else:
    print("welcome guest")
name=str(input())
if name=="sajad":
    print("welcome"+" " +name)
else:
    print("welcome guest")
name=str(input())
if name=="mdsmlsk":
    print('welcome',name)
else:
    print('welcome guest')
name=input("enter a name").lower()
if name=="dssk":
    print('welcome',name)
else:
    print("welcome guest")
names=['divya','sajad','aryansh','adrait','varna']
a=input("enter a name")
if a in names:
    print("welcome",a)
else:
    print("Welcome guest")
#vowels
vowels=['a','e','i','o','u']
name=str(input("enter a letter"))
if name in vowels:
    print("it is vowel")
else:
    print("it is not vowel")
name=str(input()).lower()
if name in vowels:
    print("it is vowel")
else:
    print("it is not vowel")
#social_media_login
username=input("enter the username")
password=int(input("enter the password"))
if username=="divya":
    if password==1234:
        print("login successful")
    else:
        print("invalid password")
else:
    print("Invalid credentials")
a="sajad";b=5678
username=input("enter the username")
password=int(input("enter the password"))
if username==a:
    if password==b:
        print("login successful")
    else:
        print("Invalid password")
else:
    print("Invalid password")
username=input("enter the username")
password=input("enter the password")
if username==username and password==password:
    print("login successful")
else:
    print("Invalid credentials")
username=input("enter the username")
password=input("enter the password")
if username=="divyasri" and password=="sajad@123":
    print("login successful")
else:
    print("Invalid Credentials")
age=int(input("enter your age "))
marks=int(input("enter your marks "))
attendance=int(input("enter your percentage "))
if age>=18:
    print("eligible age")
if marks>=80:
    print("eligible for vote")
if attendance>=70:
    print("allow to marks")
