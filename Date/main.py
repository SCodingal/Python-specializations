from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and time is" , now)

print("\nDate components", today.year, today.month,today.day)
#Difference between 2 days
date1=date(2011,11,16)
date2=date(2025,12,27)
result= date2-date1
print(result)
import calendar
print(calendar.calendar(2026))
print(calendar.month(2026,4))
print(calendar.isleap(2024))
# 0-monday,1-tuesday, 2-wednesday, 3- thursday, 4-friday, 5-saturday, 6-sunday
print(calendar.weekday(2025,12,27))
