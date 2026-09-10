from datetime import datetime

today = datetime.now()
print(f"year {today.year}")
print(f"day {today.day}")
print(f"month {today.month}")
print(f"hour {today.hour}")
print(f"min {today.minute}")
print(f"second {today.second}")


year =  today.year
day = today.day
month = today.month
hour =  today.hour
minute = today.minute
second = today.second


#now = datetime(year, day, month, hour, minute, second)

#print(today.strftime("%H:%M:%S %B %d %Y"))
parsed = today.strftime("%B %d %Y")
print(f"parsed {parsed}")