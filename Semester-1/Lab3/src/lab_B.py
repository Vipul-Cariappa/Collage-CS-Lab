# program to display calender

import calendar


# user input
year = int(input("Enter the year: "))
month = int(input("Enter the month (1 - 12): "))

output = calendar.month(year, month)

print(output)
