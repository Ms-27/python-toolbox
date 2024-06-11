from functools import wraps
from time import time


def timer(function):
    """
    Decorator to return function duration
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time()
        value = function(*args, **kwargs)
        end = time()
        duration = end - start
        print(f"{function.__name__} was executed in {duration:.4f} secs")
        return value

    return wrapper