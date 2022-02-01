# NameAndAge.py
# This program reads and then prints a users Name and Age
# author: David Burke

# Prompt the user to ender their name and age
# The result is saved to a 1x2 array called user
user = [str(input("Please input your name:")), int(input("and your Age:"))]

# Print back the users name and age with a welcome message
print("Hello {},\t your age is {}.".format(user[0],user[1]))