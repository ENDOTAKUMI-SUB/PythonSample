def calcTotal(children=2, normal=2, elder=0, *options):
  # ある遊園地の入場料を計算するプログラム
  #グローバル変数
  CHIELD_PRICE = 500 #子供料金
  ADULT_PRICE = 1000 #通常料金
  SENIOR_PRICE = 700 #年配者料金
  GROUP_MIN=10 #グループ最少人数
  GROUP_DISCOUNT = 0.8 #グループ割引率
  CONSUMPTION_TAX_RATE = 1.05  #消費税率

  # 集計(ここに「数字」は一切入れないこと!)
  total_num = children + normal + elder
  children_price = children * CHIELD_PRICE
  normal_price = normal * ADULT_PRICE
  elder_price = elder * SENIOR_PRICE
  total_price = children_price + normal_price + elder_price

  # 割引対象か確認(ここに「数字」は一切入れないこと!)
  if total_num >= GROUP_MIN:
    print("団体割引があります")
    total_price = total_price * GROUP_DISCOUNT
  else:
    print("割引はありません")

  #消費税を計算(今回の追加)
  consumption_tax = int(total_price * (CONSUMPTION_TAX_RATE - 1))
  total_price = total_price + consumption_tax

  # 結果を表示(小数点以下は表示しないこと!)
  print("子供料金 :{0}人 x 500= {1}円".format(children, children_price))
  print("通常料金 :{0}人 x1000= {1}円".format(normal, normal_price))
  print("年配者料金:{0}人 x 700= {1}円".format(elder, elder_price))
  print("消費税:{}円".format(consumption_tax))
  print("合計: {0}人 {1}円".format(total_num, total_price))

  # オプションを表示
  for o in options:
    print('オプション「{}」があります'.format(o))

calcTotal(2,2,2,"ベビーカー","車いす")