def generate_intlist(x):
	test_list = []
	try:
		print('Try ++++++++++')
		for i in range(x):
			test_list.append(i)
			if i == 10:
				raise Exception()
		print(test_list)
	except Exception as inst:
		print('Exception ++++++++++')
		print('test_list', test_list)
		print(inst)
	else:
		print('Normal Fin ++++++++++')
	finally:
		print('Finally ++++++++++')
		print('test_list', test_list)
		test_list.clear()
		print('finally: clear test_list complete')
		print('test_list', test_list)

test_list = []
generate_intlist(100)
