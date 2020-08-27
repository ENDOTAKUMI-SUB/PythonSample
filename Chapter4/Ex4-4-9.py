import calendar

year = int(input('西暦年を入力してください >'))
if year <= 0:
    print('1以上の値を入力してください')
else:
    if calendar.isleap(year) == True:
        print('{}年はうるう年です'.format(year))
    else:
        print('{}年はうるう年ではありません'.format(year))