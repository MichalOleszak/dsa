"""
1. Start with 2nd item, compare with item before it, swap if necessary
2. Look at 3rd item, compare to item before:
    - If item before is larger, swap and compare to item before that, continue swapping
    - If item before is not larger, proceed

Time complexity:
O(n^2) worst case, because it's a loop within a loop
O(n) best case, if list is (almost) sorted - for most items we don't go into while loop

Space complexity:
O(1), soriting in place, not creating additional copies of the list
"""


def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        temp = input_list[i]
        j = i - 1
        while temp < input_list[j] and j > -1:
            input_list[j + 1] = input_list[j]
            input_list[j] = temp
            j -= 1
    return input_list