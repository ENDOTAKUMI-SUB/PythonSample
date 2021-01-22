# モジュール
from random import randint

# 設定
game_digits = 3         # 桁数
hint = False             # ヒントを表示するか（デバッグ用）

'''
    答えを表示する関数
'''
def Answerprint():
    print('正解は', end='')
    print('', *answer, end='')
    print('でした。')



# HACK: Inputの関数はまとめられそう・ω・
# 引数に数値の範囲を指定するとか...
# とりあえず動くからこのままでいいか🥺
'''
    答えを入力する関数
'''
def InputAnswer(x):
    input_answer = input("{}桁目の予想入力(0~9)>>".format(x + 1))
    try:
        input_answer = int(input_answer)
    except:
        print('エラー')
        return InputAnswer(x)
    if input_answer < 0 or input_answer > 9:
        print('0 - 9')
        return InputAnswer(x)
    else:
        return input_answer


'''
    ゲームを継続するかどうか入力する関数
'''
def InputGameContinue():
    input_game_continue = input('続けますか？1:続ける 2:終了 >>')
    try:
        input_game_continue = int(input_game_continue)
    except:
        print('エラー')
        return InputGameContinue()
    if input_game_continue < 1 or input_game_continue > 2:
        print('1 - 2')
        return InputGameContinue()
    else:
        return input_game_continue


# 開始
print('数当てゲームを初めます。{}桁の数を当ててください！'.format(game_digits))

# 解答作成
answer = list()
for i in range(game_digits):
    answer.append(randint(0, 9))

# ヒント
if hint == True:
    Answerprint()

# ゲームを実行するか
is_game = True
while is_game == True:
    # キー入力
    prediction = list()
    for i in range(dgame_digits):
        data = InputAnswer(i)
        prediction.append(data)

    # 検証
    hit = 0
    blow = 0

    # ヒット数計算
    for i in range(game_digits):
        if prediction[i] == answer[i]:
            hit += 1

        # REVIEW: なんか動きキモい気がするけど気のせいかも
        # ブロー数計算
        for n in range(game_digits):
            if prediction[i] == answer[n] and i != n:
                blow += 1

    # 結果表示
    print('{}ヒット！{}ボール！'.format(hit, blow))

    # ゲームを継続するか
    if hit == game_digits:
        print('正解です！')
        is_game = False
    else:
        if InputGameContinue() == 2:
            Answerprint()
            is_game = False
