import calendar

# print(calendar.month(2022,2))

# date = input().split()

# print(calendar.isleap(2022))

c = calendar.HTMLCalendar()
for i in c.itermonthdays3(2022,2):
    print(i)