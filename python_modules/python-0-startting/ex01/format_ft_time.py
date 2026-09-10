from datetime import datetime, date
import time
print(time.time())

now = date.today()

#parsed = now.strftime("%B %d %Y")
seconds = time.time()
t = 1666355857.3622
#print(f"{t:,.4f}")

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
#test = 10
#print(f"test 10 a notation: {test:.2e}")
#print(parsed)