a = [9, 11, 7, 13, 5, 15, 3, 17, 1]
tk = int(input("探索する値を入力してください>"))
i = 0
k = -1
while i < 9 and k == -1:
    if a[i] == tk:
        k = i + 1
    i += 1
if k != -1:
    print("{}番目にあります".format(k))
else:
    print("ありません")
