# collatz.py
# This program is used to show a numbers series in the collatz conjecture
# author: David Burke

### Functions ###
# Function used to ensure the user has input the correct data and data type
# Function copied from bmi.py
def inputChecker(message):
    userInput = False
    while(userInput == False):
        try:
            userInput = int(input("{}".format(message)))
        except ValueError:
            print("Please try again. ", end="")
    return userInput

# creating a blank list for the series to be saved into
# prompt the user to input a number
# saving inital number for the final printout
numbers= []
number = inputChecker("Enter a positive whole number:")
initialNumber = number

# add the starting number to the numbers list
numbers.append(number)

# The series ends when numbers reaches 1, therefore a while loop is used            *** Ref 6
while number != 1:

    # check if the number is even, divisable by 2
    # if so devide by two and add to the list, then repeat the while loop
    if (number % 2) == 0:
        number = int(number/2)
        numbers.append(number)

    # else the number is odd
    # multipy by 3 and add 1
    else: 
        number = int((number * 3 ) + 1)
        numbers.append(number)

# if the number is equal to 1, the series can be printed.
print("The collatz series for the number {} is:\n{}".format(initialNumber, numbers))