a = int(input('aの値を入力してください >'))
b = int(input('bの値を入力してください >'))

print('--- 入れ替え前 ---')
print(f'a:{a}')
print(f'b:{b}')

# aとbの入れ替え処理
tmp = a
a = b
b = tmp

print('--- 入れ替え後 ---')
print(f'a:{a}')
print(f'b:{b}')