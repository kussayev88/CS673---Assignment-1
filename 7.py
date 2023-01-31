import os

def isLeapYear(year):
 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    else:
        return False

year = int(input('Enter year: '))

leapFlag = isLeapYear(year)

print('')

if leapFlag:
    print(year, "year is leap")
else:
    print(year, "year is NOT leap")

print('')

os.system('pause')