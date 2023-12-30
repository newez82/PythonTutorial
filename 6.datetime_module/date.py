"""
    datetime
        1. naive datetime - without timezone
"""
import datetime

import pytz

# datetime.date give us year, month and day
created_date = datetime.date(2016, 7, 24)
print("Create a date:", created_date)

today = datetime.date.today()
print("Current local date:", today)
print("Get the current local date year:", today.year)
print("Get the current local date day:", today.day)
print("Get the current local date weekday (Monday is 0, Sunday is 6):", today.weekday())
print(
    "Get the current local date iso weekday (Monday is 1, Sunday is 7):",
    today.isoweekday(),
)

# Time delta
time_delta = datetime.timedelta(days=7)
print("Get the date that is 7 days from now:", today + time_delta)

# date2 = date1 + timedelta
# timedelta = date1 + date2
bday = datetime.date(2024, 12, 1)
till_bday = bday - today
print("how many days left to my birthday from today: ", till_bday)
print("how many seconds left to my birthday from today: ", till_bday.total_seconds())

# datetime.time give us hours, minutes, seconds and microseconds
time = datetime.time(9, 30, 45, 100000)
print("Get the hours from the datetime.time: ", time.hour)


# datetime.date give us year, month and day with hours, minutes, seconds and microseconds
dtime = datetime.datetime(2016, 7, 26, 9, 30, 45, 100000)
print("Get the datetime: ", dtime)
print("Get the date without the time: ", dtime.date())
print("Get the time without the date: ", dtime.time())
print("Get the year from the datetime: ", dtime.year)

# add 12 hours from the datetime
tdelta = datetime.timedelta(hours=12)
print("Add 12 hours from the datetime: ", dtime + tdelta)

# use pytz library to work with timezone
dt_tz = datetime.datetime(2016, 7, 26, 9, 30, 45, tzinfo=pytz.UTC)
print("Get UTC time:", dt_tz)

# alterivate constructor
dtime_today = datetime.datetime.today()
dtime_now = datetime.datetime.now(tz=pytz.UTC)
# datetime.datetime.utcnow() doesn't provide timezone, need to add replace() method
# and passing the timezone parameter
dtime_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

print("Get today datetime with a timezone of none:", dtime_today)
print("Get today datetime that can pass in the timezone:", dtime_now)
print("Get today UTC datetime:", dtime_utcnow)

# Convert UTC time to different time zone
dt_pst = dtime_now.astimezone(pytz.timezone("US/Pacific"))
print("Convert UTC to PST:", dt_pst)

# without passing in the timezone parameter, we must use localized function
dt_naive = datetime.datetime.now()
pst_tz = pytz.timezone("US/Pacific")
dt_pst_localize = pst_tz.localize(dt_naive)
print("Use localized function for naive datetime:", dt_pst_localize)


# strftime - convert datetime to string
print(
    "Print dateime with ISO format - strftime - convert datetime to string:",
    dt_pst_localize.strftime("%B %d, %Y"),
)

# strptime - convert a string to a datetime
dt_str = "December 30, 2023"
dt_convert = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print("strptime - convert a string to a datetime:", dt_convert)

# print("print out a list of timezone from pytz:")
# print out a list of timezone from pytz
# for tz in pytz.all_timezones:
#    print(tz)
