year = int(input("Enter the year -: "))

if year%100 and year%400 == 0:
    leap_year = "This is a leap year"
elif year%4 == 0 and year%100 != 0:
    leap_year = "This is a leap year"
else:
    leap_year ="This is not a leap year" 
print(leap_year)       