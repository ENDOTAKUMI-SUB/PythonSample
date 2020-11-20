point = int(input('点数を入力してください>'))
if point >= 80:
    evaluation = 'A'
elif point >= 70:
    evaluation = 'B'
elif point >= 60:
    evaluation = 'C'
else:
    evaluation = 'D'
print(evaluation)