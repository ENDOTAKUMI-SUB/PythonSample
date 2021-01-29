import sys
try:
	with open('test.txt') as f:
		s = f.readline()
	print(s)
except FileNotFoundError:
	print('FileNotFoundError: ', sys.exc_info())
else:
	print('Read File Complete')
