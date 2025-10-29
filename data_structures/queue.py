"""
If implemented with a list:
- removing or adding at the end is O(1)
- removing or adding at the start is O(n) (requires reindexing)

If implemented with a linked list:
- removing at the end is O(n)
- removing at the start is O(1)
- adding at the start is O(1)
- adding at the end is O(1)
So, we dequeue (remove) from the start, and enqueue (add) at the end.
"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
