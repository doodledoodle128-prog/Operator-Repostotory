num = int(input("what is the numerator: "))
numb = int(input("What is the demoninator"))

if num%numb == 0:
    print("\n" +str(num)+ " is divisible by " +str(numb)+ "\n")\
    
else:
    print("\n" +str(num)+ " is not divisible by " +str(numb)+ "\n")