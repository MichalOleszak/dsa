"""
1. Choose a pivot element from the list - 1st item.
2. Partition the list so that all elements with values less than the pivot come before
the pivot and all elements with values greater than the pivot come after the pivot.
3. Recursively apply the quicksort algorithm to the sublists of elements with smaller
and greater values.

Pivot: O(n) - for loop over the list
Recursion: O(log n) - log n levels of recursion, e.g. 2^3 = 8
Total: O(n log n) - just like merge sort - for best and average case
Worst case: input arr alraedy sorted, the O(n) pivot is run n times, results in O(n^2)

"""

def pivot(arr, pivot_index, end_index):
    """
    - Rearrange arr in place so that all elements less than arr[pivot_index] are before 
    it and all elements greater than arr[pivot_index] are after it.
    - Return the pivot_index after the rearrangement.
    """
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
    arr[pivot_index], arr[swap_index] = arr[swap_index], arr[pivot_index]
    return swap_index

def quick_sort_helper(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort_helper(arr, left, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, right)
    return arr

def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)