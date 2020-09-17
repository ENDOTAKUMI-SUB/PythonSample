t = int(input("秒数を入力してください>"))
h = 0
m = 0
s = t
while s >= 3600:
    s -= 3600
    h += 1
while s >= 60:
    s -= 60
    m += 1
print("{}秒　→　{}時間{}分{}秒".format(t,h,m,s))