import pathlib
p = pathlib.Path('.')
print('カレントパス')
print(list(p.glob('*.py')))

p = pathlib.Path('.¥スキルアップ教科書¥Chap8')
print('プログラミングのあるディレクトリ')
print(list(p.glob('*.py')))
