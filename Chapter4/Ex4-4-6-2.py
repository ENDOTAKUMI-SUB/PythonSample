temp = int(input('いくつまでの合計を出力しますか？ >'))

result = 0
for num in range(temp):
    result += num + 1

print('1から{}までの合計は{}です'.format(temp,result ))