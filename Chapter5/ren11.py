# 関数の外側で value に 100 を代入
value = 100

def changeValue():
    # 関数の内側で value を変更
    global value 
    value = 20

changeValue();
print("value=",value) # <--- はたしてこの値は?