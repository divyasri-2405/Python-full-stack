#railway ticket

while True: 
    def railway_ticket():
        ticket_price=1000
        option=int(input("""enter the gender
1.Male
2.Female """))
        if option==1:
            age=int(input("enter the age"))
            if age>=60:
                dis=(ticket_price-(30/100)*ticket_price)
                print("you got flat 30% discount",dis)
            elif age<60:
                print("You got no discount",ticket_price)
        elif option==2:
            age=int(input("enter the age"))
            if age>=60:
                dis1=(ticket_price-(50/100)*ticket_price)
                print("you got flat 50% discount",dis1)
            elif age<60:
                dis2=(ticket_price-(30/100)*ticket_price)
                print("you got flat 30% discount",dis2)
    railway_ticket()
            
