from datetime import datetime

dt = datetime.strptime("21/11/2021 16:30", "%d/%m/%Y %H:%M")
print(dt)

print(dt.strftime("%Y 年%m 月%d 日 %H 時%M 分"))
