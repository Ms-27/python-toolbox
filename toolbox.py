import concurrent.futures
from functools import wraps
from time import time
from timeit import repeat

import tqdm


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


def handle_requests(function, issues: list, num_workers: int = 5):
    """
    Function to execute a certain function on items of a list by exploiting multithreading
    - tqdm added to visualize progress
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        return list(tqdm(executor.map(function, issues), total=len(issues)))


def time_algorithm(algorithm, array, repeat_number=3, number=10):
    """
    Function that run an algorithm a certain number of time and print minimum time execution
    """
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=repeat_number, number=number)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
