text = input('今日は何をした? >>')
with open('diary.txt', 'a', encoding="utf_8") as file:
    file.write(text + '\n')