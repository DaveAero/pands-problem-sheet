# secondstring.py
# This program reads in a string, returns every second character and inverts the order.
# author: David Burke

##### Assumptions #####
# The counting of every second charracter occurs before the inversion of the string
# The charracters to be removed are the even index numbered charracters starting from the left

# prompt user to input a sting
full_string = input("Please input text here:")

# convert string to a list                                                                                                  ***Reference 2
string = list(full_string)

# remove every second charracter using splice
# [start:stop:step] starts at index 1 (2nd charracter), the stop is not defined (as to be infinite), in steps of 2          ***Reference 3
string_2nds = string[1::2]

# all items in the array reversed, by stepping through the array in the negative direction.                                 ***Reference 4
string_2nds_rev = string_2nds[::-1]

# combining the list back into a string                                                                                     ***Reference 5
output_string = "".join(string_2nds_rev)

# print output
print(output_string)