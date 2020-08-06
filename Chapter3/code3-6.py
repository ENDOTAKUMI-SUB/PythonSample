scores = {'network': 60, 'database': 80, 'security': 50}
key = input('追加する科目名を入力してください >>')
if key in scores:
    print('すでに登録済みです')
else:
    data = int(input('得点を入力してください >>'))
    scores[key] = data
print(scores)
