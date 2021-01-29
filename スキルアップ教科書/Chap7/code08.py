import sys
try:
	with open('test1.txt') as f:
		s = f.readline()
	print(s)
except FileNotFoundError:
	print('FileNotFoundError: ', sys.exc_info())
except IOError:
	print('IOError: ', sys.exc_info())
except ValueError:
	print('ValueError: ', sys.exc_info())
except OSError:
	print('OSError: ', sys.exc_info())
except:
	print('Unexpected Error: ', sys.exc_info())
