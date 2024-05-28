from functools import wraps
from time import time


def timer(f):
    '''
        Decorator to return function duration
    '''
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        value = f(*args, **kwargs)
        end = time()
        duration = end - start
        print (f'{f.__name__} was executed in {duration:.4f} secs')
        return value
    return wrapper
