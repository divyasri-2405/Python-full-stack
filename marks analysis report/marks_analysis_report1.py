students=int(input("enter the number of students "))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student{i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print(".......................Marks Analysis Report............................")
print("Total Number of students: ",students)
print("Highest marks: ",max(marks))
print("Lowest marks: ",min(marks))
print("Total marks: ",sum(marks))
print("Average marks: ",sum(marks)/students)
