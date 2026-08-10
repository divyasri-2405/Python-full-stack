#ATM APPLICATION

while True:
    account=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        password=int(input("enter the password"))
        if password==pwd:
            options=int(input("""enter a option
1.Balance Enquiry
2.Withdrawal"""))
            if options==1:
                print("acc bal",account)
            elif options==2:
                money=int(input("enter the money"))
                print(money)
                balance=account-money
                print("rem acc bal is ",balance)
            else:
                print("Invalid options")
        else:
            print("Invalid Password")
    else:
        print("Invalid card")
