#email authentication

#otp authentication

import random
import math
import smtplib

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+" "+"is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("divyasri.motamarri@gmail.com","eapb uyug wjzx koex")
user="22501a1272@pvpsit.ac.in"
mailid=input("enter the mail which you want to send:")
s.sendmail(user,mailid,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("incorrect otp")
