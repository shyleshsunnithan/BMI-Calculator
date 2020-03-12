height = float(input("Enter height in meters : "))
weight = float(input("Enter weight in kilograms : "))

bmi = weight/(height**2)

print("Your BMI is: {0} and You are: ".format(bmi),end='')

if (bmi<16):
    print("Severely Underweight")

elif (bmi>=16 and bmi<18.5):
    print("Underweight")

elif (bmi>=18.5 and bmi<25):
    print("Healthy")

elif (bmi>=25 and bmi<30):
    print("Overweight")