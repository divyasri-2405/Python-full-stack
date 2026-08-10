#dice game

while True:
    import random
    dice_no=int(input("enter the roll of dice:"))
    a=random.randint(1,6)
    print(a)
    options=input("roll again (y/n)")
    if options=="y":
        continue
    elif options=="n":
        break
    else:
        print("Invalid options")
