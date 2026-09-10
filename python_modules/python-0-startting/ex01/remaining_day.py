from datetime import datetime

today = datetime.now()
print(f"today is {today}")

termin = datetime(2026, 8, 29, 0, 0, 0)


remain_day = termin - today

print(f"left day to your termin: {remain_day}")