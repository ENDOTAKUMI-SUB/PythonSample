money = int(input('金額を入力してください >'))
print('{}円は…'.format(money))

# 1万円札
temp = money // 10000
money = money % 10000
print('10000円札 {}枚'.format(temp))

# 5000円札
temp = money // 5000
money = money % 5000
print('5000円札 {}枚'.format(temp))

# 1000円札
temp = money // 1000
money = money % 1000
print('1000円札 {}枚'.format(temp))

# 500円玉
temp = money // 500
money = money % 500
print('500円札 {}枚'.format(temp))

# 100円玉
temp = money // 100
money = money % 100
print('100円札 {}枚'.format(temp))

# 50円玉
temp = money // 50
money = money % 50
print('50円札 {}枚'.format(temp))

# 10円玉
temp = money // 10
money = money % 10
print('10円札 {}枚'.format(temp))

# 5円玉
temp = money // 5
money = money % 5
print('5円札 {}枚'.format(temp))

# 1円玉
print('1円札 {}枚'.format(money))

print('です')