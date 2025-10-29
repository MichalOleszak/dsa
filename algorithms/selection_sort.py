"""
1. Look at 1st item, keep track of index at which minimum value is
2. Iterate over remaining items, updating min index
3. Swap min value with 1st item
4. Repeat 1-3 for remaining list items (execpt the last one, not needed)

Time complexity:
O(n^2), because it's a loop within a loop

Space complexity:
O(1), soriting in place, not creating additional copies of the list
"""


def selection_sort(input_list):
    for i in range(len(input_list) - 1):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        if min_index != i:
            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list