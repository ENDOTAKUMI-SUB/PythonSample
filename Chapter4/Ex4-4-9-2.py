def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input('西暦年を入力してください >'))
if isleap(year) == True:
    print('{}年はうるう年です'.format(year))
else:
     print('{}年はうるう年ではありません'.format(year))