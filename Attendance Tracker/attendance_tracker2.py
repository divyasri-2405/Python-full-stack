#attendance tracker

students=int(input("enter the number of students"))
p=0;a=0
for i in range(1,students+1):
    attendance=input(f"student {i} is present/absent: ")
    if attendance=="p":
        p+=1
    elif attendance=="a":
        a+=1
print("....................ATTENDANCE REPORT..........................")
print("Total Students",students)
print("Total Presentees",p)
print("Total Absentees",a)
