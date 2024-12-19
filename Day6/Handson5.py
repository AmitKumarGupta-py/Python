import logging

logging.basicConfig(filename='basic_conf.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debugging')
logging.info('Info ')
logging.warning('Warning ')
logging.error('Error ')
logging.critical('CRitical')


"""logger = logging.getLogger('advancedConfig logger')
handler = logging.FileHandler('advancedconfig.log')
formatter = logging.Formatter('%')"""