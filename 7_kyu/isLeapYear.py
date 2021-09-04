def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
    # Best Practice
    # return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0


print(isLeapYear(1984), True)
print(isLeapYear(2000), True)
print(isLeapYear(1234), False)
print(isLeapYear(1100), False)