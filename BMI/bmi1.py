'''while True:
    weight=float(input("enter the weight:"))
    height=float(input("enter the height:"))
    BMI=weight/(height**2)
    print(BMI)
    if BMI<=18.5:
        print("underweight")
    elif BMI>18.5 and BMI<=24.5:
        print("Healthy weight")
    elif BMI>24.5 and BMI<=29.5:
        print("Over weight")
    elif BMI>=30:
        print("obesity")'''

while True:
    weight=float(input("enter the weight:"))
    height=float(input("enter the height:"))
    BMI=weight/(height**2)
    print(BMI)
    if BMI<=18.5:
        print("underweight")
    elif 18.5<BMI<=24.5:
        print("Healthy weight")
    elif 24.5<BMI<=29.5:
        print("Over weight")
    elif BMI>=30:
        print("obesity")

