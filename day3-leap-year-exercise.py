year = int(input("Which year you want to check for? "))

# on every year that is evenly divisible by 4
if year % 4 == 0:
# except every year that is evenly divisible by 100
    if year % 100 == 0:
# unless the year is also evenly divisible by 400
        if year % 400 == 0:
            print(year , "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is not a leap year")
else:      
    print(year, "is not a leap year") 