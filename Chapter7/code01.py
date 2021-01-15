text = input('何を記録しますか? >>')
file = open('diary.txt', 'a', encoding="utf_8") # ←文字コード指定
file.write(text + '\n')
file.close()