month = int(input('何月ですか?>'))
if month >= 3 and month <=5 :
    season = '春'
elif month >= 6 and month <=8 :
    season = '夏'
elif month >= 9 and month <=11 :
    season = '秋'
elif month == 12 or month == 1 or month == 2 :
    season = '冬'
else:
    print('ERROR:1~12の値を入力してください')
    exit()

print('{}です'.format(season))