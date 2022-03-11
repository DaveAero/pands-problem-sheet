# bmi.py
# This program calulates a users Body Mass Index.
# author: David Burke

# Intro
print("Body Mass Index Calculator")

# Function used to ensure the user has input the correct data and data type
def inputChecker(message):
    userInput = False
    while(userInput == False):
        try:
            userInput = int(input("{}".format(message)))
        except ValueError:
            print("Please try again. ", end="")
    return userInput

# Prompt the user to enter their height and weight using the inputChecker function.
height = inputChecker("Enter height (cm):")
weight = inputChecker("Enter weight (kg):")

# Body Mass Index is a simple calculation using a person’s height and weight.
# The formula is BMI = kg/m^2 where kg is a person’s weight in kilograms and m2 is their height in metres squared.
BMI = (weight)/((height/100)**2)

# Print final result.
print("Your BMI is {}.".format(BMI))