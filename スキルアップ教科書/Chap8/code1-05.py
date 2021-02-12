import pathlib
root = pathlib.Path('/')
pp = root / 'aaa' / 'test.txt'
print(pp)

pp2 = root.joinpath('aaa', 'test.txt')
print(pp2)
