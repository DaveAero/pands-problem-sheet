# es.py
# This program is used to count the number of e's in a text file
# author: David Burke

import json
import sys

# using sys.argv to read argument from the command line
# the file path is to be entered as the the second string, following the python script              ### Ref 7
filename= str(sys.argv[1])

def readData():
    try:
        with open(filename) as f:
            data = str(f.read())
            return data
    except IOError:
        print("No file found")

# Main Code
data = readData()

# counting of the e's
# Assumption, both lower case and capital E's are required
es = int(data.count("e")) + int(data.count("E"))

#printing the final result
print(es)