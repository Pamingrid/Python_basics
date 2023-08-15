days_in_the_year=int(input("How many days are in this year? "))
second=60
hour= 60
day= 24
year=365
leapYear= 366
if days_in_the_year == year:
    result_year=(second*hour*day*year)
    print("This year have ", result_year)
else:
    days_in_the_year == leapYear
    result_leapyear=(second*hour*day*leapYear)
    print("This  leap year have", result_leapyear)