import calendar
from datetime import datetime
dayWeek = int(input('Enter day of the week: '))

now = datetime.now()
month = now.month
year = now.year

while True:
    x = calendar.weekday(year, month, 1)
    if x == dayWeek:
        print(year, month)
        break
    month -= 1
    if month == 0:
        year -= 1
        month = 12
