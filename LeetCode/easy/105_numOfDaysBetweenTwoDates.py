# https://leetcode.com/problems/number-of-days-between-two-dates/


def daysBetweenDates(date1, date2):
    
    date_1_days = get_days(date1)
    date_2_days = get_days(date2)
    return abs(date_1_days - date_2_days)


def leapYear(year):
    
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def get_days(date):
    days_array = date.split('-')
    year, month, day = map(int, days_array)
    
    leap_years = 0
    
    for i in range(1971, year):
        leap_years += int(leapYear(i))
    
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 32]
    
    result = leap_years + 365 * (year - 1971) + sum(months[:month]) + day
    
    if leapYear(year) and month > 2:
        result += 1
    return result

date1 = "2019-06-29"
date2 = "2019-06-30"
print(daysBetweenDates(date1, date2))