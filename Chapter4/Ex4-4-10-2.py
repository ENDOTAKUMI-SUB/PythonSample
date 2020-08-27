socres = []
max_score = 0
for num in range(3):
    score = int(input('{}人目の点数を入力してください > '.format(num + 1)))
    socres.append(score)
    if max_score < score:
        max_score = score

print('最高得点は{}点です'.format(max_score))