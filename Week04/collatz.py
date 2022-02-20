# collatz.py
# This program is used to show a numbers series in the collatz conjecture
# author: David Burke

# creating a blank list for the series to be saved into
numbers= []

# prompt the user to input a number
number = int(input("Please enter a positibe whole number:"))
# saving inital number for the final printout
initialNumber = number
# add the starting number to the numbers list
numbers.append(number)

# The series ends when numbers reaches 1, therefore a while loop is used
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