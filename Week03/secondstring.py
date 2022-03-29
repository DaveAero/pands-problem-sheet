# secondstring.py
# This program reads in a string, returns every second character and inverts the order.
# author: David Burke

# prompt user to input their text to be converted
inString = str(input("Input text here:"))

# convert string to a list()                                                                                                ***Ref 2
# inString[start:stop:step]                                                                                                ***Ref 3 & 4
    ## start ## is not defined so the function will start at either end of the list
    ## stop ## is not defined so the function will always use the full list
    ## step ## in steps of -2 so the list is read in the reverse direction and only evey second piece of data is being read
outString = list(inString[::-2])

# print the final string to the user
# list can be combined back into a string using the .join() function                                                          ***Ref 5
print("".join(outString))