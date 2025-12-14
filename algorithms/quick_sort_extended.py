import random


def get_pivot_random(arr):
    return random.choice(arr)


def get_pivot_first(arr):
    return arr[0]


def get_pivot_last(arr):
    return arr[-1]


def get_pivot_median_of_three(arr):
    first = arr[0]
    last = arr[-1]
    middle = arr[len(arr) // 2 - 1] if len(arr) % 2 == 0 else arr[len(arr) // 2]
    maximum = max(first, middle, last)
    minimum = min(first, middle, last)
    return first + middle + last - maximum - minimum
    

PIVOT_TACTIC_TO_FUNC = {
    "first": get_pivot_first,
    "last": get_pivot_last,
    "random": get_pivot_random,
    "median_of_three": get_pivot_median_of_three
}

def swap_arr_elements(arr, id1, id2):
    arr[id1], arr[id2] = arr[id2], arr[id1]


def partition_array_around_pivot(arr, left, right, pivot):
    if arr[left] != pivot:
        swap_arr_elements(arr, left, left + arr[left:right].index(pivot))
    i = left + 1
    for j in range(left + 1, right):
        if arr[j] < pivot:
            swap_arr_elements(arr, i, j)
            i += 1
    swap_arr_elements(arr, left, i - 1)
    return i - 1


def quick_sort_helper(arr, left, right, pivot_choice_tactic):
    n = len(arr[left:right])
    if n <= 1:
        return 0
    get_pivot_func = PIVOT_TACTIC_TO_FUNC.get(pivot_choice_tactic)
    pivot = get_pivot_func(arr[left:right])
    pivot_index = partition_array_around_pivot(arr, left, right, pivot)
    current_num_comps = n - 1
    current_num_comps += quick_sort_helper(
        arr,
        left=left,
        right=pivot_index,
        pivot_choice_tactic=pivot_choice_tactic,
    )
    current_num_comps += quick_sort_helper(
        arr,
        left=pivot_index + 1,
        right=right,
        pivot_choice_tactic=pivot_choice_tactic,
    )
    return current_num_comps


def quick_sort(arr, pivot_choice_tactic="random"):
    num_comparisons = quick_sort_helper(
        arr,
        left=0,
        right=len(arr),
        pivot_choice_tactic=pivot_choice_tactic,
    )
    return num_comparisons