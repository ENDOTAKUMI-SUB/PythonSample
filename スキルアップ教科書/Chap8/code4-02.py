import logging

logging.basicConfig(filename='test1.log', level=logging.DEBUG)
logging.debug('logfile open')
logging.info('test info output')
logging.warning('test warning output')
