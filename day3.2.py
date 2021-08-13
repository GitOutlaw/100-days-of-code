height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2

if bmi <= 18.15:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {round(bmi)}, you are normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")