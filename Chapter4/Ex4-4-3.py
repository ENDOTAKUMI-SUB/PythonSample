score = [80, 45, 60, 70, 50]
count = 0
for data in score:
     if data >= 60:
         count += 1
print('60点以上は{}人です'.format(count))