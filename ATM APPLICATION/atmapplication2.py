#ATM APPLICATION

while True:
    account=100000
    pwd=1234
    card=input("Insert the card")
    if card=="c":
        print("Welcome Divya")
        password=int(input("Enter the password"))
        if password==pwd:
            option=int(input('''Choose the option
1.balance enquiry
2.withdrawal'''))
            if option==1:
                print("acc bal is",account)
            elif option==2:
                money=int(input("enter the amount"))
                print(money)
                balance=account-money
                print("rem bal acc is",balance)
            else:
                print("Invalid option")
        else:
            print("Invalid Password")
    else:
        print("Invalid card")
