"""
Funny thing, you can not import from a file if it has dash,
like for example I had bubble-sort.py and importing did not work.
`from bubble-sort import bubble_sort` throws an error
"""

import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from tools import generate_large_list

compare = {
    "bubble": False,
    "insertion": False,
    "selection": False,
    "merge": True,
    "quick": True,
}

if __name__ == "__main__":
    list_size = 10000
    arr = generate_large_list(list_size)

    # BUBBLE SORT
    if compare["bubble"]:
        start_time = time.time()
        sorted_arr = bubble_sort(arr)
        end_time = time.time()
        print(
            f"Time taken to BUBBLE sort a list of {
              list_size} elements: {end_time - start_time:.6f} seconds"
        )

    # INSERTION SORT
    if compare["insertion"]:
        start_time = time.time()
        sorted_arr = insertion_sort(arr)
        end_time = time.time()
        print(
            f"Time taken to INSERTION sort a list of {
              list_size} elements: {end_time - start_time:.6f} seconds"
        )

    # SELECTION SORT
    if compare["selection"]:
        start_time = time.time()
        sorted_arr = selection_sort(arr)
        end_time = time.time()
        print(
            f"Time taken to SELECTION sort a list of {
              list_size} elements: {end_time - start_time:.6f} seconds"
        )

    # MERGE SORT
    if compare["merge"]:
        start_time = time.time()
        sorted_arr = merge_sort(arr)
        end_time = time.time()
        print(
            f"Time taken to MERGE sort a list of {
              list_size} elements: {end_time - start_time:.6f} seconds"
        )

    # QUICK SORT
    if compare["quick"]:
        start_time = time.time()
        sorted_arr = quick_sort(arr)
        end_time = time.time()
        print(
            f"Time taken to QUICK sort a list of {
              list_size} elements: {end_time - start_time:.6f} seconds"
        )
