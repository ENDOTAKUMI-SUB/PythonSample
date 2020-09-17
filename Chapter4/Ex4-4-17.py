a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
tk = int(input("探索する値を入力してください>"))

lo = 0
hi = 9 - 1
found = -1
while lo <= hi and found == -1:
    i = (lo + hi) // 2
    if a[i] == tk:
        found = i
    elif a[i] > tk:
        hi = i - 1
    elif a[i] < tk:
        lo = i + 1
if found >= 0:
    result = "あり"
else:
    result = "なし"
print(result)
