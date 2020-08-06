count = 0                                  # カウンタ変数
student_num = int(input('学生の数を入力 >>')) # 学生の数
score_list = list()                        # 得点リスト
while count < student_num:
    count += 1
    score = int(input('{}人目の試験の得点を入力 >>'.format(count)))
    score_list.append(score)
print(score_list)
total = sum(score_list)
print('平均点は{}点です'.format(total / student_num))