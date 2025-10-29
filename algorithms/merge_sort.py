"""
Space complexity: O(n) - additional space for the temporary arrays used for merging

Time complexoty: O(n log n) - the list is divided in half log n times and each division
takes O(n) time to merge the sublists
- Breaking list into sublists: O(log n) - e.g. 8 elements -> 3 splits
- Merging sublists: O(n) - loop through all elements with a while lopp

O(n log n) -> much better than n^2 of bubble, insertion and recursion sorts
"""

def merge(list1, list2):
    """
    Combine two sorted lists into a single sorted list.
    1. Iterate through both lists simultaneously.
    2. Compare the current element of each list.
    3. Add the smaller element to the result list.
    4. Move to the next element in the list that had the smaller element.
    5. Continue until one list is empty.
    6. Add the remaining elements of the non-empty list to the result list.
    """
    result_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result_list.append(list1[i])
            i += 1
        else:
            result_list.append(list2[j])
            j += 1
    if i < len(list1):
        result_list.extend(list1[i:])
    else:
        result_list.extend(list2[j:])
    return result_list


def merge_sort(arr):
    """
    1. Split the list in half repeatedly until each sublist has only one element.
    2. Apply merge() repetitevely to combine the sorted sublists.
    """
    if len(arr) == 1:
        return arr
    mid_index = len(arr) // 2
    left = merge_sort(arr[:mid_index])
    right = merge_sort(arr[mid_index:])

    return merge(left, right)

