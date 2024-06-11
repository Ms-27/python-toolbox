from timeit import repeat


def algorithm_timer(algorithm, array, repeat_number=3, number=10):
    """
    Function that run an algorithm a certain number of time and print minimum time execution
    """
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=repeat_number, number=number)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")