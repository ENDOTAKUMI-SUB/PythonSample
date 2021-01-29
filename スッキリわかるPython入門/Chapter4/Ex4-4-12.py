a = int(input("整数1を入力してください>"))
b = int(input("整数2を入力してください>"))
cnt = 1
ans = 0
while cnt <= b:
    ans += a
    cnt += 1
print("{}x{}={}".format(a,b,ans))