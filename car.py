print("select your ride")
print("1. Bike")
print("2. Car")


choice1 = int(input("What would you like? (1/2): "))
if choice1 == 1:
    choice2 = int(input("would you like a scooter or a scooty? (1/2): "))
    if choice2 == 1:
        print("you chose the scooter")
    elif choice2 == 2:
        print("you chose the scooty")

elif choice1 == 2:
    choice3 = int(input("Would you like a toyota or a ford? (1/2) "))
    if choice3 == 1:
        print("you chose the toyota")
    elif choice3 == 2:
        print("you chose the ford")
else:
    print("wrong option")