asterisk = int(input('*をいくつ出力しますか？ >'))

height = asterisk // 10
width = asterisk % 10

for i in range(height):
    for j in range(10):
        print('*', end='')
    print('')
print('*' * width)