a = int(input("整数1を入力してください>"))
b = int(input("整数2を入力してください>"))
syou = 0
amari = a
while amari >= b:
    amari -= b
    syou += 1
print("{}÷{}={}...{}".format(a,b,syou,amari))