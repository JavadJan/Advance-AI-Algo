""" 
Timedelta class
This object allow us to add or subtract time or date to a specific date and time

"""

from datetime import datetime, timedelta

# adding 9 hours
hour_delta = timedelta(hours=9)
print(f"hour_delta {type(hour_delta)}")

# Storing the new date
timeAdded = datetime.now() + hour_delta

# Displaying current date and time with 
# adding 9 hours
now = datetime.now()
print(f"The current time: {now}")
print(f"The date after adding 9 hours: {timeAdded}")

# adding 1 day
day_delta = timedelta(days=1)

# storing the new date
dateAdded = datetime.now() + day_delta

# Displaying current date and time with 
# adding 1 day
print(f"The date after adding 1 day: {dateAdded}")