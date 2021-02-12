class ListInfo:
	def __init__(self, my_list):
		print('__init__')
		self.my_list = my_list
	
	def __enter__(self):
		print('__enter__')
		return self

	def nth(self, n):
		return self.my_list[n]
	
	def __exit__(self, exc_type, exc_value, traceback):
		print('__exit__')
		self.my_list.clear()
		print(' exc_type: ', exc_type)
		print(' exc_valur: ', exc_value)
		print(' traceback: ', traceback)
		return True

my_list = ['a', 'b', 'c', 'd', 'e']
with ListInfo(my_list) as li:
	print('nth_inf:', li.nth(0))
print(my_list)

with ListInfo(my_list) as li:
	print('nth_inf:', li.nth(10))
print(my_list)
