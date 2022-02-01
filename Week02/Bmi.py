# Bmi.py
# This program calulates a users Body Mass Index
# author: David Burke

# Intro
print("Body Mass Index Calculator")

# Prompt the user to enter their height and weight
# The result is saved to a 1x2 array called user
user = [int(input("Please input your height (cm):")), int(input("and your weight (kg):"))]

# Body Mass Index is a simple calculation using a person’s height and weight.
# The formula is BMI = kg/m^2 where kg is a person’s weight in kilograms and m2 is their height in metres squared.
BMI = (user[1])/((user[0]/100)**2)

# Print final result
print("your BMI is {}.".format(BMI))