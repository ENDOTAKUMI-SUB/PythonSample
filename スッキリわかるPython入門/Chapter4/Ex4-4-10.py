import numpy

socres = []

for num in range(3):
    score = int(input('{}人目の点数を入力してください > '.format(num + 1)))
    socres.append(score)

max_score = numpy.argmax(socres)
print('最高得点は{}点です'.format(socres[max_score]))