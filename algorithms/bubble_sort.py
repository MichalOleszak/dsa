"""
1. Start with 1st item, compare to second item, swap if necessary
2. Compare 2nd and 3rd item, swap if necessary
3. Continue until end of list
4. We have the largest item in the list's last position, had to do n-1 comparisons
5. Repeat 1-3 for remaining n-1 items, each time we need one comparison less

Time complexity:
O(n^2), because it's a loop within a loop

Space complexity:
O(1), soriting in place, not creating additional copies of the list
"""


def bubble_sort(input_list):
    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list
