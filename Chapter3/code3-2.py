name = input('あなたの名前を教えてください >>')
print('{}さん、こんにちは'.format(name))
food = input('{}さんの好きな食べ物を教えてください >>'
             .format(name))
if food == 'カレー':
    print('素敵です。カレーは最高ですよね!!')
else:
    print('私も{}が好きですよ'.format(food))