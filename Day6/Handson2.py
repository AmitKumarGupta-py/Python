import logging


def log_to_file(log_file,log_level = logging.INFO):
    logging.basicConfig(filename = log_file, level=log_level,format= '%(asctime)s - %(levelname)s - %(messag)s' )

    def decorator(func):
        def wrapper(*args,**kwargs):
            logging.log(log_level,f"starting {func.__name__}...")
            result = func(*args,**kwargs)
            looging.log(log_level,f"finished {func.__name__}")
        return wrapper
    return decorator

@log_to_file(log_file='custom_log.log',log_level=logging.DEBUG)
def greet(name):
    print(f"Hello, {name}!!")
greet("Alice")


""""def deco2(fun2):
    def wrapper1(*args,**kwargs):







def simpl1(nam1,{k:'K'}):
    print(f"Hi...{k}")
"""""