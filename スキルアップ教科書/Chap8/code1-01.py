import pathlib
p = pathlib.Path('.')
for fd in p.iterdir():
	print(fd)
