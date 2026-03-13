med = input("Do you have a medical condition (Y/N): ").upper()
if med == "Y":
    print("You are alowed")
if med == "N":
    score = int(input("what is your attendance score: "))
    if score >= 75:
        print("you are allowed")
    else:
        print("You are not allowed")