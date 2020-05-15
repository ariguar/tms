# import calendar
# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
# birthday_date = calendar.weekday(year, month, day)
# print(calendar.day_name[birthday_date])
from calendar import day_name, weekday
birthday = input('DAY.MONTH.YEAR= ')
day, month, year = map(int, birthday.split('.'))
print(day_name[weekday(year, month, day)])
