# A given date can be valid or not. We need to look out if the month is between 1 and 12, if it's a 
# leap year, (leap year is every year that is divisible with 400, or is divisible with 4 but not 100), and 
# if the days of the month are accurate, 30 and 31.

# Write a program that for a given date outputs VALID if it's an existing date, and NOT VALID otherwise

# Input
# 1 6 1992

# Output
# VALID

# Input
# 30 2 2004
# Output
# NOT VALID

# Explanation
# The first date is valid, but the second date is not valid because February never has 30 days.

def validate_date(day, month, year):

    if month < 1 or month > 12:
        return "NOT VALID"

    days_in_month = [31, 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day < 1 or day > days_in_month[month - 1]:
        return "NOT VALID"

    return "VALID"

day, month, year = map(int, input().split())
print(validate_date(day, month, year))