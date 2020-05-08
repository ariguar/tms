import calendar

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
birthday_date = calendar.weekday(year, month, day)
print(calendar.day_name[birthday_date])
