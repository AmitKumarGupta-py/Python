import logging

"""logging.basicConfig(filename='basic_conf11.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debugging')
"""
def log_execution(func1):
    def wrappe(*args,**kwargs):
        print(f"Function Starting {func1.__name__}.....")
       # logging.basicConfig(filename='basic_conf11.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        try:
            result = func1(*args, **kwargs)
        except Exception as e:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error('You made a mistake ')


       """ logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
        logging.debug('debugging')
        logging.info('Information on file')
        logging.warning('Stay away from errors ')
        logging.error('You made a mistake ')
        logging.critical('Runnn!!')

        result  = func1(*args,**kwargs)"""
        print(f"Finished {func1.__name__}.....")
        return result
    return wrappe

### decorator without  arguments
@log_execution
def func11(para1):
    x = int("Interger")
    print(f"Hello, {para1}!!")
func11("World")