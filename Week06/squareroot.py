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
# We want to find the x axis intersection, therfore y=0. x**2 = num Or x = sqrt(num)
# Going to use a quadratic equation to find the roots of num. (ax**2)+(bx)+c=y a=1, b=0, c=-num Or y=x**2-num
# Get slope of tangent line at the point x using differentiation. dy/dx = 2x Or slope = 2x
# Equation of tangent line yTangent=slope(xTangent-x)+y. At yTangent=0 this becomes xTangent=x-(y/slope)

def sqrt(x):

    # Setting limits to the accuracy of the approximation
    # accuracy is set to + or - 1x10^9 of the entered number. This can be easily increased if needed.
    upper = num + num/1000000000
    lower = num - num/1000000000

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
x = num

# Run the above function to find an approximate square root
rootNum = sqrt(x)

# Print the result once the while loop is satisfied
print("The square root of {} is approx. {}".format(num,rootNum))