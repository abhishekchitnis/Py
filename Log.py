import logging
logging.basicConfig(handlers=[logging.FileHandler(filename="log.txt", encoding='utf-8', mode='a+')], format='%(asctime)s %(message)s', datefmt='<%a %d %b %Y %I:%M:%S %p>',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('%s before you %s', 'Look', 'leap!')
logging.error('And non-ASCII stuff, too, like Err0r')
