price = input('料金を入力 >>')
number = input('人数を入力 >>')
payment = int(price) / int(number)
print('お支払いは' + str(int(payment)) + '円です')