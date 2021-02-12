from datetime import datetime
now = datetime.today()

xday = datetime(1980, 1, 1)
td = now - xday
print(td)
