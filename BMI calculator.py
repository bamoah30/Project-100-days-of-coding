weight = float(input('Hello! '
                     'Welcome to Body Mass Index (BMI) '
                     'Please enter you weight in kg '))
height = float(input("Please enter your height in metres "))
bmi = round(weight/height**2)
print(f"Your BMI is {bmi}")
if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You have a normal weight")
elif bmi <= 30:
    print("You are overweight")
elif bmi <= 35:
    print("You are obese")
else:
    print("You are critically obese")