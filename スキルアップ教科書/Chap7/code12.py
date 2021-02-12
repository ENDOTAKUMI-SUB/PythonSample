class ExceptA(Exception):
	def __str__(self):
		return "例外 A が発生しました"

try:
	raise ExceptA
except ExceptA as ea:
	print(ea)
except:
	print('Unexpected Error:', sys.exc_info())
