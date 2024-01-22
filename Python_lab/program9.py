#Time delta
from datetime import date
from datetime import timedelta
presentdate=date.today()
print("Present date")
print(presentdate)
dateadded=presentdate+timedelta(days=20)
print("Added days")
print(dateadded)