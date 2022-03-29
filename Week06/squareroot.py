# squareroot.py
# This program is used to calculate an approximation of the square root of a given number
# author: David Burke

##### FUNCTIONS #####

### inputChecker ###
# Function used to ensure the user has input the correct data and data type
def inputChecker(message):
    userInput = False
    while(userInput == False):
        try:
            userInput = float(input("{}".format(message)))
        except ValueError:
            print("Please try again. ", end="")
    return userInput

### sqrt ###
# sqrt(num) = x  Or  x**2 = num
# Useing a quadratic equation to find the roots of num. ax**2 + bx + c = y
# We want to find the x axis intersection, therfore y=0.

# Get slope of tangent line at the guessed point x, using differentiation. dy/dx = 2x Or slope = 2x
# Equation of tangent line is yTangent=slope(xTangent-x)+y. 
# To find the y intersection, yTangent=0. This becomes xTangent=x-(y/slope)
# xTangent is then used as the next guess until the while loop is broken

def sqrt(x):

    # Setting limits to the accuracy of the approximation
    # the guess of the root is squared and compared to the entered num
    # accuracy is set to + or - 1x10^9 of the entered number. This can be easily increased if needed.
    upper = num + num/1000
    lower = num - num/1000

    # Using the limits on the while loop to find an approximation
    while x**2 > upper or x**2 < lower:
        y = x**2 - num
        slope = 2*x
        xTangent = x - (y/slope)
        x = xTangent
    return x

##### Main Code #####
# Prompt the user to enter a number using the inputChecker function.
num = inputChecker("Enter a positive number:")

# setting the inital guess equal to the number entered, as a starting point.
xZero = num

# Run the above function to find an approximate square root
rootNum = sqrt(xZero)

# Print the result once the while loop is satisfied
print("The square root of {} is approx. {}".format(num,rootNum))