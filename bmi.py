height = float(input("Enter Height in Metres (m) : "))
weight = float(input("Enter Weight in Kilograms (kg) : "))

bmi = weight/(height**2)

print("Your Body Mass Index (BMI) is: {0} and You are: ".format(bmi),end='')

if (bmi<16):
    print("Severely Underweight")

elif (bmi>=16 and bmi<18.5):
    print("Underweight")

elif (bmi>=18.5 and bmi<25):
    print("Healthy")

elif (bmi>=25 and bmi<30):
    print("Overweight")
