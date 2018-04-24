import calendar

#part b
cal = calendar.TextCalendar()  # Create an instance
cal.setfirstweekday(3)
cal.pryear(2012)

#part c

print(cal.formatmonth(2018, 12))

#part d
"""
d = calendar.LocaleTextCalendar(6, "SPANISH")
d.pryear(2012)"""
#Error ??

#part e

print(calendar.isleap(2022))
#tells you if year is leap year -- cool