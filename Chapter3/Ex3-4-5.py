hour = int(input('24時間形式の時刻を入力してください>'))
if hour > -1 and hour < 25:
    if hour < 12:
        print('午前{}時'.format(hour))
    else:
        print('午後{}時'.format(hour))
else:
    print('0～24の値を入力してください')
