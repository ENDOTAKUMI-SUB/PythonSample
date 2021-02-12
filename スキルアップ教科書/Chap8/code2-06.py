import datetime
t_delta = datetime.timedelta(days=1)
dt = datetime.datetime.strptime("15/2/21 16:30", "%d/%m/%y %H:%M")
dt += t_delta
print(dt)
