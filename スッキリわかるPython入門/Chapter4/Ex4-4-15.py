a = [9, 11, 7, 13, 5, 15, 3, 17, 1]
tk = int(input("探索する値を入力してください>"))
i = 0
result = "なし"
while i < 9 and result == "なし":
    if a[i] == tk:
        result = "あり"
    i += 1
print(result)
