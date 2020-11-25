def eat(breakfast, lunch, dinner='カレー', desserts=()):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べました'.format(d))


eat('トースト', 'パスタ', 'カレー', ('アイス', 'チョコ', 'パフェ'))