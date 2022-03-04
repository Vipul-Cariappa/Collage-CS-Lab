# Program to check whether the given year is leap year

year = int(input("Enter the year to check: "))

if year % 100 != 0 and year % 4 == 0:
    print(f"Given year {year} is a leap year.")
elif year % 400 == 0:
        print(f"Given year {year} is a leap year.")
else:
    print(f"Given year {year} is not a leap year.")
