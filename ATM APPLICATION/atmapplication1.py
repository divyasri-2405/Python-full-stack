account=100000
card='c'
pwd=1234
ca_rd=input("insert the card")
if ca_rd=='c':
    print("Welcome Divya")
    pawd=input("enter the password")
    if pwd==1234:
        option=int(input('''1.Balance Enquiry
                      2.Withdraw'''))
        if option==1:
            print(f"Balance Enquiry {account}")
        elif option==2:
            withdraw=input("enter the amount")
            print(f"Withdraw {withdraw}")
        else:
            print("Invalid options")
    else:
        print("Invalid password")
else:
    print("Invalid card")


            


