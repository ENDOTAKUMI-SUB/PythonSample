import logging
import myprocess

def main():
	logging.basicConfig(filename='test2.log', level=logging.INFO)
	logging.info('main.py call myprocess function')
	myprocess.process1()
	logging.info('main.py main function exit')
if __name__ == '__main__':
	main()
