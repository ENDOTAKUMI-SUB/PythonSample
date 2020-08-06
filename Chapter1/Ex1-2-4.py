monthCount = int(input('月数を入力してください >'))
yearResult = monthCount // 12
monthResult = monthCount % 12
print('{}か月は{}年{}か月です'.format(monthCount, yearResult, monthResult))