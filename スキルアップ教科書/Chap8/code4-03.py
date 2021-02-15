import logging

logging.basicConfig(filename='test1.log', level=logging.WARNING)
logging.debug('logfile open : lovel = warning')
logging.info('test info output : level = warning')
logging.warning('test warning output : level = warning')
