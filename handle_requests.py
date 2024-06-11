import concurrent.futures

import tqdm


def handle_requests(function, issues: list, num_workers: int = 5):
    """
    Function to execute a certain function on items of a list by exploiting multithreading
    - tqdm added to visualize progress
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        return list(tqdm(executor.map(function, issues), total=len(issues)))