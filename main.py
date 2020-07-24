import sys

while True:
    year = input("Please input an integer representing a year after 1581. (Enter 0 to Exit)")
    year = int(year)
    if year == 0:
        break

    while (int(year) < 1582):
        print("That is not a valid input.")
        year = input("Please input an integer representing a year after 1581. (Enter 0 to Exit)")
        year = int(year)
        if year == 0:
            sys.exit()

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("The year is a leap year(it has 366 days).")
            else:
                print("The year is not a leap year (it has 365 days).")
        else:
            print("The year is a leap year(it has 366 days).")
    else:
            print("The year is not a leap year (it has 365 days).")
