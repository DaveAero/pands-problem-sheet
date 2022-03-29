# es.py
# This program is used to count the number of e's in a text file
# author: David Burke

# importing libarys 
import sys

# using sys.argv to read argument from the command line
# the file path is to be entered as the the second string, following the python script              ### Ref 9
# Example: $ python es.py shrek.txt
filename= str(sys.argv[1])

# using a function to read the text file
# the file will be read as a string saved as data
def readData():
    with open(filename) as f:
        data = str(f.read())
        return data

### Main Code ###
data = readData()

# counting of the e's
# Assumption, both lower case and capital E's are required
es = int(data.count("e")) + int(data.count("E"))

#printing the final result
print(es)