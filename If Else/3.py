year=int(input("enter year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("the year is a leap year")
else:
    print("given year is not a leap year.")