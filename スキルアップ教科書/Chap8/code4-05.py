import logging

logging.basicConfig(filename='test3.log', level=logging.WARNING)
test_data = [1, 3, 6]
try:
	raise Exception
except:
	logging.exception('test exeption message :%s', test_data)
