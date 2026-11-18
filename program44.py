
import time
import datetime

now = datetime.datetime.now()

print("a) Current date and time:", now)
print("b) Current year:", now.year)
print("c) Month of the year:", now.month)
print("d) Week number of the year:", now.strftime("%W"))
print("e) Weekday of the week:", now.strftime("%a"))
print("f) Day of the year:", now.strftime("%j"))
print("g) Day of the month:", now.day)
print("h) Day of the week:", now.weekday())


