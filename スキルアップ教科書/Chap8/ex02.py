from datetime import datetime
t_str = '20210215165959'
dt = datetime.strptime(t_str, "%Y%m%d%H%M%S")
print(dt)
print(dt.strftime("%Y%m%d%H%M%S"))
