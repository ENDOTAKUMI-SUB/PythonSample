import sys
try:
	with open('test1.txt') as f:
		s = f.readline()
	print(s)
except (FileNotFoundError, IOError, ValueError, OSError) as err:
	print(':', sys.exc_info())
	print('err', err)
except:
	print('Unexpected Error: ', sys.exc_info)
