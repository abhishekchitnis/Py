import logging
logging.basicConfig(handlers=[logging.FileHandler(filename="log.txt", encoding='utf-8', mode='a+')], format='%(asctime)s %(message)s', datefmt='<%a %d %b %Y %I:%M:%S %p>',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('%s before you %s', 'Look', 'leap!')
logging.error('And non-ASCII stuff, too, like Err0r')

'''
Levels = When they're used

DEBUG = Detailed information, typically of interest only when diagnosing problems.

INFO = Confirmation that things are working as expected.

WARNING = An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

ERROR = Due to a more serious problem, the software has not been able to perform some function.

CRITICAL = A serious error, indicating that the program itself may be unable to continue running.

More Info : https://docs.python.org/3/howto/logging.html

'''
