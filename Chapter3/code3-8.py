name = input('あなたの名前を教えてください >>')
print('{}さん、こんにちは'.format(name))
if name == '松田':
    print('松田さんに会えてうれしいです')
food = input('{}さんの好きな食べ物を教えてください >>'
             .format(name))
if 'カレー' in food:
    print('素敵です。とにかくカレーは最高ですよね!!')
else:
    print('私も{}が好きですよ'.format(food))