# Inversion == a pair of indices (i, j) such that i < j and arr[i] > arr[j]
# total inversions = left inversions + right inversions + split inversions
# split inversions == inversions where one element is in the left half and the other is in the right half

def _merge_and_count_split_inversions(b, c):
    d = []
    num_split_inversions, i, j = 0, 0, 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1
            num_split_inversions += len(b) - i
    if i == len(b):
        d += c[j:]
    else:
        d += b[i:]
    return d, num_split_inversions


def _count_inversions(arr):
    if len(arr) == 1:
        return arr, 0
    midpoint = len(arr) // 2
    b, x = _count_inversions(arr[:midpoint])
    c, y = _count_inversions(arr[midpoint:])
    d, z = _merge_and_count_split_inversions(b, c)
    return d, x + y + z


def count_inversions(arr):
    _, num_inversions = _count_inversions(arr)
    return num_inversions