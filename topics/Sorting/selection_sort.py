import time
from tools import generate_large_list


def selection_sort(arr):
    sorted_arr = list(arr)
    n = len(arr)

    for i in range(n):
        current_min_ind = i
        for j in range(i, n):
            if sorted_arr[j] < sorted_arr[current_min_ind]:
                current_min_ind = j

        sorted_arr[i], sorted_arr[current_min_ind] = (
            sorted_arr[current_min_ind],
            sorted_arr[i],
        )

    return sorted_arr


if __name__ == "__main__":
    # list_size = 1000
    # arr = generate_large_list(list_size)

    arr = [6, 8, 5, 2, 7, 1, 9]
    list_size = len(arr)

    print("arr: ", arr)
    print()
    start_time = time.time()
    sorted_arr = selection_sort(arr)
    end_time = time.time()
    print()
    print("sorted_arr: ", sorted_arr)

    print(
        f"Time taken to sort a list of {list_size} elements: {
          end_time - start_time:.6f} seconds"
    )
