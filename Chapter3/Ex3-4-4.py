hour = int(input('24時間形式の時刻を入力してください>'))
if hour < 12:
    print('午前')
else:
    print('午後')