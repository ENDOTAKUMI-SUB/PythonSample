import logging

logging.basicConfig(filename='test1.log', level=logging.WARNING, format='%(levelname)s: %(asctime)s: %(message)s')
logging.warning('test warning output')
