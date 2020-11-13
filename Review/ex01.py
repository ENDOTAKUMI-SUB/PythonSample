# 人数の入力
child = int(input("子供料金(13才未満)は何人? "))
adult = int(input("通常料金(13-64才)は何人?"))
elderly = int(input("年配者料金(65 才以上)は何人?"))
people = child + adult + elderly


# 集計
child_price = child * 500
adult_price = adult * 1000
elderly_price = elderly * 700
price = child_price + adult_price + elderly_price


# 割引対象科確認
if people >= 10:
    print("団体割引があります")
    price *= 0.8
else:
    print("割引はありません")


# 結果を表示
print("子供料金　：{} x 500 = {}円".format(child, child_price))
print("通常料金　：{} x 1000= {}円".format(adult, adult_price))
print("年配者料金：{} x 700 = {}円".format(elderly, elderly_price))
print("合計　　　：{}人 {}円".format(people, price))
