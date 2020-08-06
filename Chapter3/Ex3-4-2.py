number1 = int(input('整数を入力してください>'))
number2 = int(input('整数を入力してください>'))
if number1 < number2:
    print('{}の方が大きいです'.format(number2))
elif number1 > number2:
    print('{}の方が大きいです'.format(number1))
else:
    print('同じ値が入力されました')