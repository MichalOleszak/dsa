"""
- Heap is a complete binary tree (complete = filled from left to right with no gaps).
- Each node has a value larger than all of its descendants.
- Largest value is at the root (in max heap; in min heap, min is at the top).
- Nodes can have duplicated values.
- Not useful for searching (no guarantee of structure or order other than at root).
- Useful for keep track of the largets or smallest value.
- Useful for implementing priority queues (where you always dequeue the largest value)
- Stored in a list:
    - Approach 1: Root at index 0, left child at index 1, right child at index 2, etc.
    - Approach 2: Root at 1, skip 0 index -> easier lookup.
- Lookup for Approach 2:
    - left_child = 2 * parent_index
    - rihgt_child = 2 * parent_index + 1
    - parent = child_index // 2
"""


class MaxHeap():
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(max_index)
            right_index = self._right_child(max_index)
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        """
        O(log n) - max number of swaps is equal to the height of the tree
        1. Insert at the next open space (bottom right) to ensure the tree is complete.
        2. Swap moving the new node up (bubble it up) until it reaches correct position.
        """
        self.heap.append(value)
        new_value_index = len(self.heap) - 1
        while new_value_index > 0 and value > self.heap[self._parent(new_value_index)]:
            self._swap(new_value_index, self._parent(new_value_index))
            new_value_index = self._parent(new_value_index)

    def remove(self):
        """
        O(log n) - max number of swaps is equal to the height of the tree
        1. Only remove the root node.
        2. Rearange the heap to make sure it a complete tree:
            2a. Move the "last" node - bottom right - to the root.
            2b. Swap moving the new root down until it reaches its correct position.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
