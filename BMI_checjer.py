height = float(input("what is your height in cm?: "))
weight = float(input('what is your weight in kg?: '))

BMI = weight / (height/100)**2

if BMI <= 18.4:
    print('underweight')
elif BMI <= 24.9:
    print('Healthy')
elif BMI <= 29.9:
    print ("overweight")
else:
    print("severly overweight")