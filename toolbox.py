from functools import wraps
from time import time

#
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

###===###

import concurrent.futures
import tqdm

#multithread for a list + tqdm
def handle_requests(func, issues: list, num_workers: int = 5):
    '''
        Function to execute a function on several items of an list by exploiting multithreading 
    '''
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        return list(tqdm(executor.map(function, issues), total=len(issues)))

###===###

from timeit import repeat

def time_algorithm(algorithm, array):
    '''
        Function that run an algorithm a certain number of time and print minimum time execution 
    '''
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
