# isLeapYear

This program asks the user for an integer representing a year on or after 1582 – this is the year that the Gregorian calendar was adopted. 
Any year less than this results in an error message followed by asking the user to re-enter a more appropriate value.
The program will then determine whether the year input by the user is a leap year (or not) in the Gregorian calendar. 

The rules for determining a leap year are as follows: 

If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
The year is a leap year (it has 366 days).
The year is not a leap year (it has 365 days).
