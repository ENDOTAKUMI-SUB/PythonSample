bodyWeight = int(input('体重を入力してください>'))
bodyHeight = int(input('身長を入力してください>'))
bmi = bodyWeight / (bodyHeight * bodyHeight) * 10000
print(bmi)

if bmi < 18.5:
    print('痩せ気味です')
elif bmi >= 18.5 and bmi < 25.0:
    print('普通です')
elif bmi >= 25.0 and bmi < 35.0:
    print("太り気味です")
else:
    print('高度肥満です')