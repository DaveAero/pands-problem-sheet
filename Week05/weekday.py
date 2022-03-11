# weekday.py
# This program is used to check if it is currently a weekday
# author: David Burke

# importing datetime as a usefull function
from datetime import datetime

#creatinge a variable for the current day of the week using datetime
weekday = datetime.today().weekday()

## Weekdays as outputted by daytime.today().weekday()
#weekdays = {0 : "Monday",
#            1 : "Tuesday",
#            2 : "Wednesday",
#            3 : "Thursday",
#            4 : "Friday",
#            5 : "Saturday",
#            6 : "Sunday"}

# Use the number index of weekday() to check if today is a weekday
if weekday <= 4:
    print("Yes, unfortunately today is a weekday.")

# if not, it must be a weekend
else:
    print("It is the weekend, yay!")