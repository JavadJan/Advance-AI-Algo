from datetime import date
from time import altzone

today = date.today()

print(altzone.imag)
print(today.month)
print(today.day)
print(today.year)

my_termin = date(2026, 8, 1)

print(f"day left to get you driver licence: {my_termin - today}")
""" 
time 1 component
set 1 component for list of to do list: to prevernt repeated task
dic can {day: list}
 """