import logging

logging.basicConfig(filename='practice1.log', level=logging.WARNING)
logging.warning('1')
logging.error('2')
logging.debug('3')
logging.info('4')
logging.shutdown()
